```
//================================================================
// FUNCIONES DE UTILIDAD Y CONFIGURACIÓN
//================================================================
SubProceso crearSeparador(separador, _longitud)
	Escribir "";
	Para i <- 1 Hasta _longitud Hacer
		Escribir separador Sin Saltar;
	FinPara
	Escribir "";
FinSubProceso


Funcion longitudMaxima <- encontrarMaxLongitudEnArreglo(arreglo, _dimension)
	longitudMaxima <- Longitud(arreglo[1]);
	Para i <- 1 Hasta _dimension - 1 Con Paso 1 Hacer
		Si longitudMaxima < Longitud(arreglo[i + 1]) Entonces
			longitudMaxima <- Longitud(arreglo[i + 1]);
		FinSi
	FinPara
FinFuncion

SubProceso centrarTexto(_texto, ancho)	
	Definir i, margen Como Entero;
	margen <- ancho - Longitud(_texto);
	Escribir "" Sin Saltar; 
	Para i <- 1 Hasta margen/2 Hacer
		Escribir " " Sin Saltar;
	FinPara
	Escribir _texto Sin Saltar;
	Escribir "";
FinSubProceso

//================================================================
// FUNCIONES DE LA FASE 1: ENTRADA A LA DISCOTECA
//================================================================

Funcion nombreCliente <- preguntarNombre
	Definir respuesta Como Caracter;
	Mientras Longitud(respuesta) = 0 O Longitud(respuesta) > 50 Hacer		
		Escribir "Ingresa tu nombre:";
		Leer respuesta;		
		Si Longitud(respuesta) > 50 Entonces
			Escribir "Dale suave"			
		FinSi
		Esperar 2 Segundos
		Limpiar Pantalla
	FinMientras
	Si Longitud(respuesta) > 0 Entonces
		nombreCliente <- respuesta;
		Limpiar Pantalla;
		Escribir "
	FinSi
FinFuncion

SubProceso darBienvenida(nombreDiscoteca, longitudSeparador)
	crearSeparador("*", longitudSeparador);
	centrarTexto(nombreDiscoteca, longitudSeparador);
	crearSeparador("*", longitudSeparador);
FinSubProceso


Funcion esMayorDeEdad <- validarEdad(FRASES_ENTRADA, _dimension)
	Definir fraseAleatoria, edad Como Entero;
	fraseAleatoria <- azar(_dimension) + 1; 
	Escribir FRASES_ENTRADA[fraseAleatoria];
	Leer edad;
	Repetir
		Limpiar Pantalla
		Si edad < 0 Entonces
			Escribir "Habla bien U.U solo se admiten valores positivos"
			Leer edad
			Limpiar Pantalla
		FinSi
		Si edad > 99 Entonces
			Escribir "Jajaja que buena broma, pero ya en serio dime tu edad!"
			Leer edad
			Limpiar Pantalla
		FinSi
		
	Hasta Que edad > 0 Y edad < 100
	Si edad < 18 Entonces		
		Escribir "¡Solo se permiten mayores de edad!";		
		esMayorDeEdad <- Falso;
		Esperar 3 Segundos
	SiNo		
		esMayorDeEdad <- Verdadero;
	FinSi	
	Limpiar Pantalla;
FinFuncion

Funcion quierePagar <- cobrarEntrada(precioEntrada)
    Definir respuesta Como Caracter;
    Escribir "Perfecto. La entrada cuesta $", precioEntrada, "...";
    Escribir "¿Deseas pagar? (Escribe si o no)";
    Leer respuesta;    
	Limpiar Pantalla;
    Repetir
		Escribir "Oh discúlpame, pero no te entendí. ¿Deseas pagar? (Escribe si o no)";
		Leer respuesta;
		Limpiar Pantalla;
	Hasta Que Minusculas(respuesta) = "si" O Minusculas(respuesta) = "no"
	    
    Escribir "";
    Si Minusculas(respuesta) = "si" Entonces
        Escribir "¡Genial! Aquí tienes tu pulsera...";
        quierePagar <- Verdadero;
		Esperar 2 Segundos;
    SiNo
        Escribir "Es una lástima. Que tengas una buena noche...";
        quierePagar <- Falso;
		Esperar 2 Segundos;
    FinSi
	Limpiar Pantalla;
FinFuncion

//================================================================
// FUNCIONES DE LA FASE 2: DENTRO DE LA DISCOTECA
//================================================================
Funcion accion <- preguntarAccion(credito, bebidasConsumidas)
	Definir accion Como Entero;
	Escribir "";
	crearSeparador("=", 50);
	centrarTexto("Tu estado actual:", 50);
	crearSeparador("-", 50);
	Escribir "Estás en la pista. La música suena genial *_*";
	Escribir " - Crédito restante: $", credito;
	Escribir " - Bebidas consumidas:", bebidasConsumidas, "/3";
	crearSeparador("=", 50);
	Escribir "¿Qué quieres hacer ahora?";
	Escribir "";
	Escribir "1. Comprar una bebida";
	Escribir "2. Bailar en la pista";
	Escribir "3. Intentar ligar en la barra";
	Escribir "4. Irse a casa";
	Leer accion;
	Esperar 1 Segundos;
	Limpiar Pantalla;
FinFuncion

Funcion opcionComprada <- comprarBebida(creditoActual, bebidasActuales, NOMBRES_BEBIDAS, PRECIOS_BEBIDAS)
	Definir opcionBebida, i, dimensionMenu Como Entero;
	Definir costoBebida Como Real;
	
	dimensionMenu <- 3;
	opcionComprada <- 0;
	
	Si bebidasActuales >= 3 Entonces
		Escribir "Ya has bebido suficiente por esta noche (límite de 3). ¡No seas lámpara!";
	SiNo
		crearSeparador("-_", 25);
		centrarTexto("\o/ MENU DE TRAGUITOS \o/", 50);
		crearSeparador("_", 50);
		
		Escribir "¿Qué bebida quieres?";
		Escribir "";
		Para i <- 1 Hasta dimensionMenu Hacer
			Escribir i, ". ", NOMBRES_BEBIDAS[i], " ($", PRECIOS_BEBIDAS[i], ")";
		FinPara
		Escribir dimensionMenu + 1, ". Mejor no, volver al menú";
		Leer opcionBebida;
		Esperar 1 Segundos
		Limpiar Pantalla
		Si opcionBebida >= 1 Y opcionBebida <= dimensionMenu Entonces
			costoBebida <- PRECIOS_BEBIDAS[opcionBebida];
			
			Si creditoActual >= costoBebida Entonces
				Escribir "¡Salud! Disfrutas de tu ", NOMBRES_BEBIDAS[opcionBebida], ". Te sientes genial.";
				opcionComprada <- opcionBebida; 
			SiNo
				Escribir "No tienes suficiente crédito para esa bebida. ¡Qué chiro!";
			FinSi
		SiNo
			Escribir "Decides no comprar nada por ahora...";
		FinSi
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
FinFuncion

// *** FUNCIÓN DE ANIMACIÓN ***
SubProceso animarBaile
	Definir frames Como Caracter;
	Definir i, j Como Entero;
	Dimension frames[7]; 
	
	frames[1] <- "  .`+.´.`+.´    (>`-`)>    .+´.`.+´.`  ";
	frames[2] <- "  .´ .`+.´ .`+    <(´_´<)    .`.´+.`.´+  ";
	frames[3] <- "  .`+.´.`+.´   ^(*_*)\-    .+´.`.+´.`  ";
	frames[4] <- "  .´ .`+.´ .`+    \m/(-_-)\m/    . `.´+.`.´+  ";
	frames[5] <- "  .`+.´.`+.´    <( `-`)>    .+´.`.+´.`  ";
	frames[6] <- "  .´ .`+.´ .`+    \_( .``)>    . `.´+.`.´+  ";
	frames[7] <- "  .`+.´.`+.´    <( ._.)-`    .+´.`.+´.`  ";
	Limpiar Pantalla
	// Repetir la secuencia de baile 2 veces		
	Para i <- 1 Hasta 2 Hacer
	
		Para j <- 1 Hasta 7 Hacer // Actualizamos el límite del bucle a 7
			Limpiar Pantalla;
			crearSeparador("-_",50);
			Escribir "";
			centrarTexto(frames[j], 100);
			crearSeparador("-_",50);
			Esperar 1 Segundos;
		FinPara
	FinPara
	Limpiar Pantalla;
FinSubProceso

SubProceso accionBailar
	Definir fraseAleatoria Como Entero;
	fraseAleatoria <- azar(3);	
	Segun fraseAleatoria Hacer
		0: Escribir "¡Te lanzas a la pista y sacas los pasos prohibidos! La gente alucina.";
		1: Escribir "Justo suena un temazo. ¡Bailas con una energía increíble y todos te hacen espacio!";
		2: Escribir "Intentas un paso de baile nuevo, te tropiezas, pero lo conviertes en un movimiento cool. ¡Nadie se dio cuenta!";
	FinSegun
	Esperar 5 Segundos
	Limpiar Pantalla
	animarBaile(); // Llamamos a la animación antes de mostrar el texto	
FinSubProceso

SubProceso accionLigar
	Definir fraseAleatoria Como Entero;
	Esperar 1 Segundos;
	Limpiar Pantalla;
	fraseAleatoria <- azar(4);
	Segun fraseAleatoria Hacer
		0: Escribir "Te acercas con tu mejor labia... ¡y funciona! Te da su número. ¡Éxito total!";
		1: Escribir "La persona te sonríe, pero te dice: solo salí a bailar con mis panas. Bueno, se intentó.";
		2: Escribir "La conversación es increíble. No consigues su número, pero te ríes un montón y te sube el ánimo.";
		3: Escribir "La música está tan alta que no se oyen. Terminan haciendo señas y riendo. Fue raro, pero divertido.";
	FinSegun
	Esperar 5 Segundos;
	Limpiar Pantalla;
FinSubProceso

//================================================================
// SUBPROCESO PARA LA FACTURA
//================================================================
Funcion facturaGenerada <-  generarFactura(registro, cantidadBebidas, NOMBRES, PRECIOS, costoEntrada)	
	Definir totalFactura Como Real;
	Definir indiceBebida, i Como Entero;
	Definir nombreBebida Como Caracter;
	Definir precioBebida Como Real;
	
	Limpiar Pantalla
	//Encabezado
	Escribir "";
	crearSeparador("=", 45);
	Escribir "       RESUMEN DE TU NOCHE EN DISCO SIGMA";
	crearSeparador("=", 45);
	Escribir "DETALLE DE CONSUMO:";
	Escribir "";
	
	totalFactura <- costoEntrada;
	Escribir " - Entrada General ................. $", costoEntrada;
	
	//Solo si consumió bebidas
	Si cantidadBebidas > 0 Entonces
		Para i <- 1 Hasta cantidadBebidas Hacer			
			
			indiceBebida <- registro[i]; 
			nombreBebida <- NOMBRES[indiceBebida];
			precioBebida <- PRECIOS[indiceBebida];
			
			Escribir " - ", nombreBebida, " ....................... $", precioBebida;
			totalFactura <- totalFactura + precioBebida;
		FinPara
	SiNo
		Escribir " (No consumiste ninguna bebida en la barra)";
	FinSi
	
	Escribir "";
	crearSeparador("-", 45);
	Escribir " TOTAL GASTADO: $", totalFactura;
	crearSeparador("=", 45);
	facturaGenerada <- Verdadero
FinFuncion

//================================================================
// ALGORITMO PRINCIPAL
//================================================================
Algoritmo Disco_Sigma
	Definir nombreDiscoteca, nombreCliente Como Caracter;
	Definir precioEntrada Como Real;
	Definir dimensionFrasesEntrada Como Entero;
	Definir esMayorDeEdad, quierePagar, esFinDelPrograma, facturaGenerada Como Logico;
	
	nombreDiscoteca <- " *_*_ DISCO SIGMA *_*_";
	precioEntrada <- 10.0;
	dimensionFrasesEntrada <- 5;	
	Dimension FRASES_ENTRADA[dimensionFrasesEntrada];
	nombreCliente <- preguntarNombre;
	
	FRASES_ENTRADA[1] <- "¡Qué más mi pana "+ nombreCliente+ "! Cédula en mano! ¿Cuántos años tienes?.";
	FRASES_ENTRADA[2] <- "¡La noche está bacansisima! A ver, ¿cuántos años tienes, "+ nombreCliente + "?.";
	FRASES_ENTRADA[3] <- "¡Ponte once brother! Dime tu edad, " + nombreCliente +".";
	FRASES_ENTRADA[4] <- "¡Chévere que vengas mi pex! A ver esa identificación. ¿Cuál es tu edad, " + nombreCliente + "?.";
	FRASES_ENTRADA[5] <- "¿Qué fue, " + nombreCliente + "? Muéstrame la cédula, de una. Dime tu edad.";
	
	Definir longitudSeparadorBienvenida Como Entero;	
	longitudSeparadorBienvenida <- encontrarMaxLongitudEnArreglo(FRASES_ENTRADA, dimensionFrasesEntrada);
	darBienvenida(nombreDiscoteca, longitudSeparadorBienvenida);
	
	esMayorDeEdad <- validarEdad(FRASES_ENTRADA, dimensionFrasesEntrada);
	
	Si esMayorDeEdad Entonces
		Escribir "Bienvenido a ", nombreDiscoteca
		crearSeparador("-_", 25)
		quierePagar <- cobrarEntrada(precioEntrada);
	SiNo
		quierePagar <- Falso;
	FinSi
	
	Si esMayorDeEdad Y quierePagar Entonces
		Definir bebidasConsumidas, accion, creditosAccion, opcionFinal Como Entero; 
		Definir credito, costoCompra Como Real;				
		Dimension NOMBRES_BEBIDAS[3], PRECIOS_BEBIDAS[3];
		Dimension registroDeCompras[3];
		
		credito <- 21;
		bebidasConsumidas <- 0;
		esFinDelPrograma <- Falso;
		creditosAccion <- 4;
		
		NOMBRES_BEBIDAS[1] <- "Cerveza";     PRECIOS_BEBIDAS[1] <- 3.00;
		NOMBRES_BEBIDAS[2] <- "Cuba Libre";  PRECIOS_BEBIDAS[2] <- 5.00;
		NOMBRES_BEBIDAS[3] <- "Whisky";      PRECIOS_BEBIDAS[3] <- 8.00;				
		
		Mientras NO esFinDelPrograma Hacer
			accion <- preguntarAccion(credito, bebidasConsumidas);
			creditosAccion <- creditosAccion - 1;
			
			Segun accion Hacer
				1:					
					opcionFinal <- comprarBebida(credito, bebidasConsumidas, NOMBRES_BEBIDAS, PRECIOS_BEBIDAS);
					
					Si opcionFinal > 0 Entonces
						costoCompra <- PRECIOS_BEBIDAS[opcionFinal];
						credito <- credito - costoCompra;
						bebidasConsumidas <- bebidasConsumidas + 1;
						registroDeCompras[bebidasConsumidas] <- opcionFinal;
					SiNo
						creditosAccion <- creditosAccion + 1;
					FinSi
				2:
					accionBailar;
				3:
					accionLigar;
				4:
					Escribir "Decides que ya fue suficiente. ¡Una retirada a tiempo es una victoria!";
					esFinDelPrograma <- Verdadero;
				De Otro Modo:
					Escribir "Opción inválida. Te quedas un momento pensando qué hacer.";
					creditosAccion <- creditosAccion + 1;
			FinSegun
			
			Si bebidasConsumidas >= 3 Entonces
				crearSeparador("-", 50);
				Escribir "Has llegado a tu límite de 3 bebidas. La noche ha sido buena, pero es hora de irse.";
				esFinDelPrograma <- Verdadero;
			FinSi
			
			Si creditosAccion <= 0 Y NO esFinDelPrograma Entonces
				crearSeparador("-", 50);
				Limpiar Pantalla
				Escribir "De repente, las luces se encienden un poco. El DJ anuncia la última canción.";
				Escribir "¡El tiempo voló! La discoteca va a cerrar. ¡Qué buena farra!";
				Esperar 5 Segundos
				esFinDelPrograma <- Verdadero;
			FinSi
		FinMientras
		
		Si esMayorDeEdad Y quierePagar Entonces
			facturaGenerada <- generarFactura(registroDeCompras, bebidasConsumidas, NOMBRES_BEBIDAS, PRECIOS_BEBIDAS, precioEntrada);
		FinSi
	FinSi
	
	Escribir "";
	crearSeparador("*", 50);
	centrarTexto("GRACIAS POR VENIR, "+Mayusculas(nombreCliente)+". HASTA LA PRÓXIMA", 50);
	crearSeparador("*", 50);
FinAlgoritmo

```