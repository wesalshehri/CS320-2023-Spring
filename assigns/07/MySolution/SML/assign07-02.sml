(* ****** ****** *)
use
"./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
//
HX-2023-03-31: 20 points
Please implement the following function
that enumerates all the pairs (i, j) of natural
numbers satisfying $i <= j$; a pair (i1, j1) must
be enumerated ahead of another pair (i2, j2) if the
following condition holds:
  i1*i1*i1 + j1*j1*j1 < i2*i2*i2 + j2*j2*j2
//
val
theNatPairs_cubesum: (int * int) stream = fn () =>
//
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-assign07-02.sml] *)


fun
helper1
( n0: int
, start: int
, fopr: int -> 'a): 'a stream =
let
fun
fmain1
(i0: int): 'a stream = fn() =>
strcon_cons(fopr(i0), fmain1(i0+1))
fun
fmain2
(i0: int): 'a stream = fn() =>
if
i0 >= n0
then strcon_nil else
strcon_cons(fopr(i0), fmain2(i0+1))
in
if n0 < 0 then fmain1(start) else fmain2(start)
end



val theNatPairs_cubesum: (int * int) stream =
    let
        fun helper(temp : int) : (int * int) stream = fn() =>
            if temp = 0 then
                strcon_cons((0, 0), helper(temp + 1))
            else
                strcon_cons((0, temp), stream_merge2(helper1(~1, temp, fn(num) => (temp, num)), helper(temp + 1), fn((i1, j1), (i2, j2)) =>
                pow_int_int(i1, 3) + pow_int_int(j1, 3) <= pow_int_int(i2, 3) + pow_int_int(j2, 3)))
    in 
    helper(0)
    end

