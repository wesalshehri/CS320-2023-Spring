(* ****** ****** *)
use "./../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
Please put your implementation here for quiz04-02
*)

(* ****** ****** *)

(* end of [CS320-2023-Spring-quizzes-quiz04-02.sml] *)


fun stream_dupremov(fxs: int stream): int stream =
  let
    fun aux(prev: int, fxs: int stream): int stream =
      if stream_forall(fxs, fn x => x = prev)
      then stream_nil()
      else
        let
          val curr = stream_head(fxs)
          val rest = stream_tail(fxs)
        in
          if curr = prev
          then aux(prev, rest)
          else stream_cons(curr, aux(curr, rest))
        end
  in
    aux(~1, fxs)
  end
