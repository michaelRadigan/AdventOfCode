// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open System.IO
open System.Reflection

[<EntryPoint>]
let main _ =
    let day = 2    

    // This is to get up from the exe directory    
    let projectName = Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName
    let path = Path.Combine(projectName, "Inputs", $"{day}.in");
    let lines = File.ReadAllLines(path);
    
    let solutionA = AOC.Two.solveA lines
    printfn $"solutionA: {solutionA}"
    
    // let solutionB = AOC.one.solveB lines
    // printfn $"solutionB: {solutionB}"

    0 // return an integer exit code