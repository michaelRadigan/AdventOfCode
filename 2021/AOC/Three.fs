module AOC.Three

    open System

    let private flipBits (n : int) : int = 
        let mask = (1 <<< 12) - 1
        n ^^^ mask

    let solveA (lines : string seq) =
        // TODO[michaelr]: We can grab this instead of hardcoding :)        
        [0 .. 11]
        |> Seq.map (fun i ->
            lines
            |> Seq.countBy (fun line -> line.[i])
            //|> Seq.maxBy (fun (bit, freq) -> freq, if bit = '0' then )
            |> Seq.maxBy snd
            |> fst
        )
        |> Array.ofSeq
        |> String
        |> (fun epsilon -> Convert.ToInt32(epsilon, 2))
        |> (fun epsilon -> epsilon * (epsilon |> flipBits))
        
        
