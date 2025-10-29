## Logica Propocional

Involucion no p = p

Idempotencia: pvp = p, p ^ p

conmutativa: pvq = qvp

asociativa: pvq v r = p v qvr

distributiva: pvq ^ r = p^r v q^r

morgan: ~ pvq = ~p^~q

PyT = P, PvT = T, PyF = F, PvF = P

[(~p^q) -> F] ^ ~q
[(pv~q) v F] ^ ~q
(p v ~q) ^ ~q
~q

~[~(~p v q) -> p] v q
~[(~p v q) v p] v q morgan
[(p ^ ~q) ^ ~p] v q morgan x 2
[(p^~p)^ ~q] v q conmutativa
[F ^ ~q] v q complemento
 F v q      identidad
 q      identidad

