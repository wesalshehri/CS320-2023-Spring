(* ****** ****** *)
use
"./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
HX-2023-03-24: 10 points
The following is a well-known series:
ln 2 = 1 - 1/2 + 1/3 - 1/4 + ...
Please implement a stream consisting of all the partial
sums of this series.
The 1st item in the stream equals 1
The 2nd item in the stream equals 1 - 1/2
The 3rd item in the stream equals 1 - 1/2 + 1/3
The 4th item in the stream equals 1 - 1/2 + 1/3 - 1/4
And so on, and so forth
//
*)

(* ****** ****** *)

(*
val the_ln2_stream: real stream = fn() => ...
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-assign06-01.sml] *)



val the_ln2_stream: real stream = fn() =>
  let
    fun partial_sum_helper(i, sgn, acc) =
      strcon_cons(i, fn() => partial_sum_helper(i+sgn*1.0/acc,~sgn, acc+1.0))
  in
    partial_sum_helper(1.0,~1.0,2.0)
  end


