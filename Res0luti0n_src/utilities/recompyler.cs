using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var recompyled = new Dictionary<string, string>();
            var allParts = new string[] { "PARTS_PATH" };
            foreach (var part in allParts)
            {
                var content = File.ReadAllText(part, Encoding.UTF8);
                var step1 = Base64Decode(content);
                recompyled.Add(part, CaesarDecoder(step1));
            }

            var recompyledContent = new StringBuilder();
            foreach (var part in allParts)
            {
                recompyledContent.Append(recompyled[part]);
            }

            // Write the recompyled Python code to a temporary file
            var tempFilePath = Path.GetTempFileName();
            File.WriteAllText(tempFilePath, recompyledContent.ToString(), Encoding.UTF8);

            // Run the Python script in a separate process
            var processInfo = new ProcessStartInfo("python", tempFilePath);
            processInfo.UseShellExecute = false;
            processInfo.RedirectStandardOutput = true;

            using (var process = new Process())
            {
                process.StartInfo = processInfo;
                process.Start();

                var output = process.StandardOutput.ReadToEnd();
                Console.WriteLine(output);

                process.WaitForExit();
            }

            // Delete the temporary file
            File.Delete(tempFilePath);
        }

        static string Base64Decode(string encodedText)
        {
            var decodedBytes = Convert.FromBase64String(encodedText);
            return Encoding.ASCII.GetString(decodedBytes);
        }

        static string CaesarDecoder(string encodedText)
        {
            var decryptionKey = encodedText.Substring(encodedText.Length - 2);
            var shift = decryptionKey.Sum(c => (int)c) % 26;
            var decodedText = new StringBuilder();
            foreach (var c in encodedText.Substring(0, encodedText.Length - 2))
            {
                if (char.IsLetter(c))
                {
                    if (char.IsLower(c))
                    {
                        var decryptedC = (char)(((int)c - 97 - shift + 26) % 26 + 97);
                        decodedText.Append(decryptedC);
                    }
                    else
                    {
                        var decryptedC = (char)(((int)c - 65 - shift + 26) % 26 + 65);
                        decodedText.Append(decryptedC);
                    }
                }
                else
                {
                    decodedText.Append(c);
                }
            }
            return decodedText.ToString();
        }
    }
}