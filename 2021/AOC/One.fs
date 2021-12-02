module AOC.one
    let solveA (lines : string seq) =
        lines
        |> Seq.map int
        |> Seq.pairwise
        |> Seq.filter (fun (current, next) -> next > current)
        |> Seq.length
                   
    let solveB (lines : string seq) =
        let intLines = lines |> Seq.map int
        Seq.zip intLines (intLines |> Seq.skip 3)
        |> Seq.filter (fun (current, next) -> next > current)
        |> Seq.length
        

