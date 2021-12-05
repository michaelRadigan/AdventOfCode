module AOC.Two
    
    type StateA =
        {
            Depth : int;
            Dist : int;
        }
          
    type StateB =
        {
            Depth : int
            Dist : int
            Aim : int
        }
        
    let solve (lines : string seq) folder empty total =
       lines
       |> Seq.map (fun line ->
            let splitLine = line.Split(' ')
            splitLine.[0], splitLine.[1] |> int
       )
       |> Seq.fold folder empty 
       |> total
        
    let solveA (lines : string seq) =
        let folder (state : StateA) ((command, num) : string * int) : StateA =
            match command with
            | "up" -> {Depth = state.Depth - num; Dist = state.Dist}
            | "down" -> {Depth = state.Depth + num; Dist = state.Dist}
            | _ -> {Depth = state.Depth; Dist = state.Dist + num}
       
        solve lines folder {Depth = 0; Dist = 0} (fun state -> state.Depth * state.Dist)
                           
    let solveB (lines : string seq) =
        let folder (state : StateB) ((command, num) : string * int) : StateB =
            match command with
            | "up" -> {Depth = state.Depth; Dist = state.Dist; Aim = state.Aim - num }
            | "down" -> {Depth = state.Depth; Dist = state.Dist; Aim = state.Aim + num}
            | _ -> {Depth = state.Depth + num * state.Aim; Dist = state.Dist + num; Aim = state.Aim}
        
        solve lines folder {Depth = 0; Dist = 0; Aim = 0} (fun state -> state.Depth * state.Dist)