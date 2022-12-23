use std::collections::HashSet;

use itertools::Itertools;

#[derive(Debug, PartialEq, Copy, Clone, Hash, Eq)]
struct Position { x: i32, y: i32}

impl Position {
    fn move_by(&mut self, dx: i32, dy: i32)  {
        self.x += dx;
        self.y += dy;
    }

    fn distance(&self, other: &Position) -> (i32, i32) {
        (self.x - other.x, self.y - other.y)
    }
}

#[derive(Debug, PartialEq, Copy, Clone)]
struct Rope {H: Position, T: Position}

#[derive(Debug, PartialEq, Copy, Clone)]
struct LongRope {positions: [Position; 10]}

#[derive(Debug, Clone)]
struct State {rope: Rope, visited: HashSet::<Position>}

struct LongState {rope: LongRope, visited: HashSet<Position>}

fn move_rope(state: &mut State, dx: i32, dy: i32, dist: u32) {
    for _ in 0..dist {    
        state.rope.H.move_by(dx, dy);    
        let (dist_x, dist_y) = state.rope.H.distance(&state.rope.T);
        match (dist_x, dist_y) {
            (x, _y) if x > 1  => state.rope.T = Position { x: state.rope.H.x - 1, y : state.rope.H.y},
            (x, _y) if x < -1 => state.rope.T = Position { x: state.rope.H.x + 1, y : state.rope.H.y},
            (_x, y) if y > 1  => state.rope.T = Position { x: state.rope.H.x, y : state.rope.H.y - 1},
            (_x, y) if y < -1 => state.rope.T = Position { x: state.rope.H.x, y : state.rope.H.y + 1},
            _ => ()
        }
        state.visited.insert(state.rope.T);
    }
}

pub fn part1(input: &str) -> usize {
    let mut state = State {
        rope : Rope {
            H : Position{ x : 0, y : 0},
            T : Position {x : 0, y : 0}
        },
        visited : HashSet::<Position>::new()
    };
    state.visited.insert(Position {x: 0, y: 0});

    input
    .lines()
    .for_each(|line| {
        match line.split(' ').collect_tuple() {
            Some(("R", dist)) => move_rope(&mut state, 1, 0, dist.parse().unwrap()),
            Some(("L", dist)) => move_rope(&mut state, -1, 0, dist.parse().unwrap()),
            Some(("U", dist)) => move_rope(&mut state, 0, 1, dist.parse().unwrap()),
            Some(("D", dist)) => move_rope(&mut state, 0, -1, dist.parse().unwrap()),
            wat => panic!("It didn't match: {:?}", wat)
        }
    });
    state.visited.len()
}

fn move_long_rope(state: &mut LongState, dx: i32, dy: i32, dist: u32) {
    for _ in 0..dist {
        state.rope.positions[0].move_by(dx, dy);
        for leader_idx in 0..9 {
            let leader = state.rope.positions[leader_idx];
            let follower = state.rope.positions[leader_idx + 1];

            let (dist_x, dist_y) = leader.distance(&follower);
                
            // Please forgive me :( :( 
            let new_follower =  match (dist_x, dist_y) {
                (x, y) if x > 1 && y > 1 => Position { x: leader.x - 1, y : leader.y - 1},
                (x, y) if x > 1 && y < -1 => Position { x: leader.x - 1, y : leader.y + 1},
                (x, y) if x < -1 && y > 1 => Position { x: leader.x + 1, y : leader.y - 1},
                (x, y) if x < -1 && y < -1 => Position { x: leader.x + 1, y : leader.y + 1},
                (x, _y) if x > 1 => Position { x: leader.x - 1, y : leader.y},
                (x, _y) if x > 1  => Position { x: leader.x - 1, y : leader.y},
                (x, _y) if x < -1 => Position { x: leader.x + 1, y : leader.y},
                (_x, y) if y > 1  => Position { x: leader.x, y : leader.y - 1},
                (_x, y) if y < -1 => Position { x: leader.x, y : leader.y + 1},
                 _ => follower
            };
            state.rope.positions[leader_idx + 1] = new_follower;
        }
        state.visited.insert(state.rope.positions[9]);
    }
}

pub fn part2(input: &str) -> usize {


    let long_rope:[Position;10] = [Position{x:0,y:0};10];
    let mut state = LongState {
        rope : LongRope {positions: long_rope},
        visited : HashSet::<Position>::new()
    };
    state.visited.insert(Position {x: 0, y: 0});

    input
    .lines()
    .for_each(|line| {
        match line.split(' ').collect_tuple() {
            Some(("R", dist)) => move_long_rope(&mut state, 1, 0, dist.parse().unwrap()),
            Some(("L", dist)) => move_long_rope(&mut state, -1, 0, dist.parse().unwrap()),
            Some(("U", dist)) => move_long_rope(&mut state, 0, 1, dist.parse().unwrap()),
            Some(("D", dist)) => move_long_rope(&mut state, 0, -1, dist.parse().unwrap()),
            wat => panic!("It didn't match: {:?}", wat)
        }
    });
    state.visited.len()
}
