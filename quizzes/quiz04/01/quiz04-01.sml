(* ****** ****** *)
use "./../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
Please put your implementation here for quiz04-01
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-quizzes-quiz04-01.sml] *)

val theAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fun alphabeta_cycling_list(): char stream =
  let
    val alphabet_stream = string_streamize(theAlphabet)
  in
    stream_append(alphabet_stream, alphabeta_cycling_list())
  end
