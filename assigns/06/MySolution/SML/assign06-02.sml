(* ****** ****** *)
use
"./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
HX-2023-03-24: 10 points
Please enumerate all the pairs of natural
numbers. Given pairs (i1, j1) and (i2, j2),
(i1, j1) should be enumerated ahead of (i2, j2)
if i1+j1 < i2+j2.
*)

(* ****** ****** *)

(*
val theNatPairs: (int*int) stream = fn () => ...
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-assign06-02.sml] *)


val theNatPairs: (int*int) stream = fn () =>
  let
    fun helper1(n: int): (int*int) stream =
      stream_tabulate((n+1), fn(i) => (i, (n-i)))

    val helper2 = stream_tabulate(~1, fn(i) => helper1(i))
  in
    stream_concat(helper2)()
  end
