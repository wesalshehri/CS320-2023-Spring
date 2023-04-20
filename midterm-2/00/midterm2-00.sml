(* ****** ****** *)

use "./../../mysmlib/mysmlib-cls.sml";

(* ****** ****** *)

(*
//
// HX-2023-04-20: 20 points
// 10 points for stream_take
// 10 points for stream_drop
//
Given a stream fxs, stream_take(fxs, n)
returns another stream containing the first
n items in fxs (or all the elements of fxs if
fxs contains fewer than n elements).
//
Given a stream fxs, stream_drop(fxs, n)
returns another stream containing all but the
first n elements of fxs.
//
*)

(* ****** ****** *)

(*
fun
stream_take
(fxs: 'a stream, n: int): 'a stream = ...
*)

(* ****** ****** *)

(*
fun
stream_drop
(fxs: 'a stream, n: int): 'a stream = ...
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-midterm2-00.sml] *)





fun stream_take(fxs: 'a stream, n: int): 'a stream = if n <= 0 then stream_nil() else case fxs() of strcon_nil => stream_nil()  | strcon_cons(x, fx) => stream_cons(x, stream_take (fx, n - 1)) 

fun stream_drop(fxs: 'a stream, n: int): 'a stream = if n <= 0 then fxs else case fxs() of strcon_nil => stream_nil()  | strcon_cons(x, fx) => stream_drop (fx, n - 1) 
