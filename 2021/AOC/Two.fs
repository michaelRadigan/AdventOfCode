module AOC.Two

    type StateA =
        {
            Depth : int
            Dist : int
        }
        
    let solveA (lines : string seq) =
        let pairs = 
            lines
            |> Seq.map (fun line ->
                let splitLine = line.Split(' ')
                splitLine.[0], splitLine.[1] |> int
           )
        
        let folder (state : StateA) ((command, num) : string * int) : StateA =
            match command with
            | "up" -> {Depth = state.Depth - num; Dist = state.Dist}
            | "down" -> {Depth = state.Depth + num; Dist = state.Dist}
            | _ -> {Depth = state.Depth; Dist = state.Dist + num}
        
        let finalState =
            Seq.fold folder {Depth = 0; Dist = 0} pairs
        
        finalState.Depth * finalState.Dist    
                           
    let solveB (lines : string seq) =
        failwith "Not implemented"