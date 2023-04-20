-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-04-2023 a las 11:31:02
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdtaquillaweb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tcines`
--

CREATE TABLE `tcines` (
  `id` int(11) NOT NULL,
  `cineNombre` varchar(25) NOT NULL,
  `cineLogo` varchar(255) NOT NULL,
  `cantidadSalas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tcines`
--

INSERT INTO `tcines` (`id`, `cineNombre`, `cineLogo`, `cantidadSalas`) VALUES
(1, 'Cines Austin', 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/logos/logo_Austin.jpg', 3),
(2, 'Cines TMA', 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/logos/logo_TMA.jpg', 5),
(3, 'Cines Mix', 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/logos/logo_Mix.jpg', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tentradas`
--

CREATE TABLE `tentradas` (
  `id` int(11) NOT NULL,
  `id_pelicula` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_cine` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `entradaPrecioUnitario` double NOT NULL,
  `entradaCantButacas` int(11) NOT NULL,
  `entradaPrecioTotal` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tpeliculas`
--

CREATE TABLE `tpeliculas` (
  `id` int(11) NOT NULL,
  `titulo` varchar(25) NOT NULL,
  `estreno` tinyint(1) NOT NULL,
  `sinopsis` varchar(2000) NOT NULL,
  `peliculaPrecio` double NOT NULL,
  `cartel` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tpeliculas`
--

INSERT INTO `tpeliculas` (`id`, `titulo`, `estreno`, `sinopsis`, `peliculaPrecio`, `cartel`) VALUES
(1, 'Austin Powers', 0, 'Primera aventura de Austin Powers (Mike Myers), un peculiar y atractivo espía de los años sesenta, cuyo principal enemigo es el doctor Maligno (interpretado también por Myers). Tras ser ambos sometidos a un proceso de congelación, se despiertan treinta años después en una sociedad completamente distinta a la que conocían. Sin embargo, ellos siguen siendo los mismos.', 6.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/austin_powers.jpg'),
(2, 'El Guateque', 0, 'Hrundi V. Bakshi es un patoso actor de origen hindú que se encuentra rodando una película en el desierto. Por sus continuas meteduras de pata, es despedido del rodaje. Inesperadamente, recibe una invitación para asistir a una sofisticada fiesta organizada por el productor de su última película. Gracias a Hrundi, en la fiesta se producirán las situaciones más disparatadas.', 6.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/el_guateque.jpg'),
(3, 'La Vida de Brian', 1, 'Brian nace en un pesebre de Belén el mismo día que Jesucristo. Un cúmulo de desgraciados y tronchantes equívocos le harán llevar una vida paralela a la del verdadero Hijo de Dios. Sus pocas luces y el ambiente de decadencia y caos absoluto en que se haya sumergida la Galilea de aquellos días, le harán vivir en manos de su madre, de una feminista revolucionaria y del mismísimo Poncio Pilatos, su propia versión del calvario.', 8.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/la_vida_de_Brian.jpg'),
(4, 'Blade Runner', 0, 'Rick Deckard (Harrison Ford) es un blade runner, un agente de policía destinado al retiro de replicantes ilegales. Su misión es dar caza a un grupo de cuatro de estos androides, sofisticados NEXUS 6 superiores en fuerza e inteligencia a los humanos, pero diseñados para vivir una corta existencia de cuatro años.', 7.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/blade_runner.jpg'),
(5, 'Matrix', 0, 'Thomas Anderson es un brillante programador de una respetable compañía de software. Pero fuera del trabajo es Neo, un hacker que un día recibe una misteriosa visita...', 7.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/matrix.jpg'),
(6, 'Tron', 1, 'Sam Flynn, un experto en tecnología de 27 años e hijo de Kevin Flynn, investiga la desaparición de su padre y se adentra en un mundo digital distinto al original y creado por su padre, de feroces programas y juegos de arcade, y donde su padre ha estado atrapado durante 20 años.', 8.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/tron.jpg'),
(7, '2001 A Space Odyssey', 0, 'Hace millones de años, antes de la aparición del \"homo sapiens\", unos primates descubren un monolito que los conduce a un estadio de inteligencia superior. Millones de años después, otro monolito, enterrado en una luna, despierta el interés de los científicos. Por último, durante una misión de la NASA, HAL 9000, una máquina dotada de inteligencia artificial, se encarga de controlar todos los sistemas de una nave espacial tripulada.', 7.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/2001_a_space_odyssey.jpg'),
(8, 'Poltergeist', 0, 'La película fue el primer gran éxito de Spielberg como productor. La trama gira en torno a los inquietantes sucesos que acontecen en la casa de una familia que vive en los suburbios, y en la que se sospecha que se está produciendo el fenómeno conocido como «poltergeist».', 7.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/poltergeist.jpg'),
(9, 'Regreso al Futuro', 0, 'La cinta transcurre en el año 1985, una época en la que el joven Marty McFly lleva una existencia anónima con su novia Jennifer. Los únicos problemas son su familia en crisis y un director al que le encantaría expulsarle del instituto, por lo que deberá hacer todo lo que esté en su mano para revertir esa situación y aparentar total normalidad. Amigo del excéntrico profesor Emmett Brown, una noche le acompaña a probar su nuevo experimento: viajar en el tiempo usando un DeLorean modificado...', 7.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/regreso_al_futuro.jpg'),
(10, 'Memorias de Africa', 1, 'A principios del siglo XX, Karen (Streep) contrae un matrimonio de conveniencia con el barón Blixen (Brandauer), un mujeriego empedernido. Ambos se establecen en Kenia con el propósito de explotar una plantación de café. En Karen Blixen nace un apasionado amor por la tierra y por las gentes de Kenia.', 8.5, 'https://www.jfernandez.colexio-karbo.com/22-23/taquillaweb-img/carteles/memorias_de_africa.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tsalas`
--

CREATE TABLE `tsalas` (
  `id` int(11) NOT NULL,
  `numeroSala` int(11) NOT NULL,
  `aforoSala` int(11) NOT NULL,
  `id_cine` int(11) NOT NULL,
  `id_pelicula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tsalas`
--

INSERT INTO `tsalas` (`id`, `numeroSala`, `aforoSala`, `id_cine`, `id_pelicula`) VALUES
(1, 1, 50, 1, 1),
(2, 2, 60, 1, 2),
(3, 3, 70, 1, 3),
(4, 1, 65, 2, 4),
(5, 2, 75, 2, 5),
(6, 3, 90, 2, 6),
(7, 4, 80, 2, 7),
(8, 5, 80, 2, 6),
(9, 1, 70, 3, 4),
(10, 2, 70, 3, 3),
(11, 3, 80, 3, 8),
(12, 4, 80, 3, 9),
(13, 5, 100, 3, 10),
(14, 6, 100, 3, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tusuarios`
--

CREATE TABLE `tusuarios` (
  `id` int(11) NOT NULL,
  `usuarioNombre` varchar(25) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(50) NOT NULL,
  `token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tcines`
--
ALTER TABLE `tcines`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tentradas`
--
ALTER TABLE `tentradas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tPeliculas_id_pelicula_tEntradas` (`id_pelicula`),
  ADD KEY `tCines_id_cine_tEntradas` (`id_cine`),
  ADD KEY `tUsuarios_id_usuario_tEntradas` (`id_usuario`);

--
-- Indices de la tabla `tpeliculas`
--
ALTER TABLE `tpeliculas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tsalas`
--
ALTER TABLE `tsalas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tCines_id_cine_tSalas` (`id_cine`),
  ADD KEY `tPeliculas_id_pelicula_tSalas` (`id_pelicula`);

--
-- Indices de la tabla `tusuarios`
--
ALTER TABLE `tusuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tcines`
--
ALTER TABLE `tcines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tentradas`
--
ALTER TABLE `tentradas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tpeliculas`
--
ALTER TABLE `tpeliculas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `tsalas`
--
ALTER TABLE `tsalas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `tusuarios`
--
ALTER TABLE `tusuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tentradas`
--
ALTER TABLE `tentradas`
  ADD CONSTRAINT `tCines_id_cine_tEntradas` FOREIGN KEY (`id_cine`) REFERENCES `tcines` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `tPeliculas_id_pelicula_tEntradas` FOREIGN KEY (`id_pelicula`) REFERENCES `tpeliculas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `tUsuarios_id_usuario_tEntradas` FOREIGN KEY (`id_usuario`) REFERENCES `tusuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tsalas`
--
ALTER TABLE `tsalas`
  ADD CONSTRAINT `tCines_id_cine_tSalas` FOREIGN KEY (`id_cine`) REFERENCES `tcines` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `tPeliculas_id_pelicula_tSalas` FOREIGN KEY (`id_pelicula`) REFERENCES `tpeliculas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
