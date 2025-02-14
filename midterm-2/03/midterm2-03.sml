(* ****** ****** *)

use "./../../mysmlib/mysmlib-cls.sml";

(* ****** ****** *)
(*
HX-2023-04-20:
Given a finite or infinite stream fxss of
infinite streams: fxs_0, fxs_1, fxs_2, ...,
stream_zipstrm(fxss) returns an infinite stream
of streams: gxs_0, gxs_1, gxs_2, ..., where we have
gxs_j[i] = fxs_i[j]. Note that this is just the
stream version of stream_ziplst (see Assign07-01).
*)
(* ****** ****** *)

(*
fun
stream_zipstrm
( fxss
: 'a stream stream): 'a stream stream = ...
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-midterm2-03.sml] *)


fun helper(fxss, x) = strcon_cons(foreach_to_foldleft(stream_foreach)(fxss, fn() => strcon_nil, fn(x1, temp) => stream_append(x1, fn() => strcon_cons(stream_get_at(temp, x), fn() => strcon_nil))), fn() => helper(fxss, x+1)) handle Subscript => strcon_nil


fun stream_zipstrm(fxss: 'a stream stream): 'a stream stream = fn() => helper(fxss, 0)




