(* ****** ****** *)
use
"./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
HX-2023-04-07: 20 points
Given a list xs, stream_permute_list(xs) returns
a stream of ALL the permutations of xs.
For instance, if xs = [1,2,3], then the returned
stream should enumerate the following 6 lists:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2] and [3,2,1]
//
fun
stream_permute_list(xs: 'a list): 'a list stream = ...
//
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-assign08-01.sml] *)




fun helper1(x, []) = [[x]]
| helper1(x, (y::ys)) = (x::y::ys) :: list_map((helper1(x, ys)), (fn ys => y::ys))

fun helper2([]) = list_streamize [[]]
| helper2(x::xs) = stream_concat(stream_make_map(helper2 xs, fn x1 => list_streamize(helper1(x, x1))))

fun stream_permute_list(xs: 'a list): 'a list stream = helper2 xs



