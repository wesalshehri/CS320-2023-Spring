(* ****** ****** *)
use "./../../MySolution/SML/generator.sml";
(* ****** ****** *)
use "./../../../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

(*
There is an implementation of infinite generators
in [generator.sml]. Please study the implementation.
How do you use it to give an implementation of generators
that are possibily finite?
*)

(* ****** ****** *)

type 'a fgenerator = 'a option generator

(* ****** ****** *)

(*
//
HX-2023-04-15: 20 points
//
Please implement the following function that converts
a stream into a generator that is possibly finite.
(*
There is not much code to write here; the problem mainly
test your understanding of continuations.
*)
//
fun
fgenerator_make_stream(fxs: 'a stream): 'a fgenerator = ...
//
*)

(* ****** ****** *)



fun helper(fxs, x1, x2) = case fxs() of strcon_nil => let val() = generator_yield(NONE, x1, x2) in NONE end | strcon_cons(x0, fxs) => let val() = generator_yield(SOME(x0), x1, x2) in helper(fxs, x1, x2) end


fun fgenerator_make_stream(fxs: 'a stream): 'a fgenerator = generator_make_fun(fn(x1, x2) => helper(fxs, x1, x2))


(* end of [CS320-2023-Spring-assigns-assign09-02.sml] *)
