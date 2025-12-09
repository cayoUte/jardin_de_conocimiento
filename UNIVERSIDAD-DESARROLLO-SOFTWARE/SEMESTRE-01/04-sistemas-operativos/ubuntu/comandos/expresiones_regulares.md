grep -E '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' nombre_del_archivo.txt

`^`: Coincide con el inicio de la línea.
`[A-Za-z0-9._%+-]`+: Coincide con la parte del nombre de usuario, que puede incluir letras (mayúsculas y minúsculas), números y los símbolos ._%+-. El + indica que debe haber uno o más de estos caracteres.
@: Coincide con el símbolo "@" literal.
[A-Za-z0-9.-]+: Coincide con la parte del nombre de dominio, que puede incluir letras, números, puntos y guiones. El + indica que debe haber uno o más de estos caracteres.
\.: Coincide con un punto literal (.) que separa el nombre del dominio de la extensión.
[A-Za-z]{2,}: Coincide con la extensión del dominio (como .com, .org), que debe tener al menos dos letras.
$: Coincide con el final de la línea.
-E: Le dice a grep que interprete la expresión regular como extendida, lo que permite usar símbolos como + y {} sin necesidad de escaparlos. 