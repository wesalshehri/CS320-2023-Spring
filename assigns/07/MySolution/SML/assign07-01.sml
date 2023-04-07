(* ****** ****** *)
use
"./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
HX-2023-03-31: 10 points
Please implement the following function
that turns a list of streams into stream of
lists.
//
fun
stream_ziplst('a stream list): 'a list stream
//
If we use a list of streams to represent a
list of rows of a matrix, then the returned
stream consist of lists that are columns of the
matrix.
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-assign07-01.sml] *)



fun stream_ziplst(xs: 'a stream list): 'a list stream = fn() =>
  let
    fun helper(xs, i) =
      strcon_cons(
        list_foldright(xs, [], fn(y, temp) => stream_get_at(temp, i) :: y),
        fn() => helper(xs, i + 1)
      )
      handle Subscript => strcon_nil
  in
    helper(xs, 0)
  end

