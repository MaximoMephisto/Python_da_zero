-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Lug 27, 2026 alle 09:12
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cinema_esempio`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `log_operazioni`
--

CREATE TABLE `log_operazioni` (
  `id` int(11) NOT NULL,
  `operazione` varchar(50) DEFAULT NULL,
  `tempo` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `log_operazioni`
--

INSERT INTO `log_operazioni` (`id`, `operazione`, `tempo`) VALUES
(1, 'Registrato utente ciccio', '2026-07-24 12:53:16'),
(2, 'Registrato utente sara', '2026-07-24 12:53:27');

-- --------------------------------------------------------

--
-- Struttura della tabella `storico_operazioni`
--

CREATE TABLE `storico_operazioni` (
  `id` int(11) NOT NULL,
  `nome_op` varchar(50) DEFAULT NULL,
  `tempo` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `storico_operazioni`
--

INSERT INTO `storico_operazioni` (`id`, `nome_op`, `tempo`) VALUES
(1, 'Registrazione utente: ciccio', '2026-07-24 12:53:16'),
(2, 'Registrazione utente: sara', '2026-07-24 12:53:27');

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE `utenti` (
  `id` int(11) NOT NULL,
  `username` varchar(40) DEFAULT NULL,
  `passwd` varchar(100) DEFAULT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0
) ;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`id`, `username`, `passwd`, `admin`) VALUES
(1, 'ciccio', 'cf8276ca60061baf2611917c50717a2b1bcbff0c0d25e00b95ef667ab8f158f0', 0),
(2, 'sara', 'f6a8bae47ae1165e9bf38a7e7d0911fa1e00fc5146d5607b3878de623ca1f531', 0);

--
-- Trigger `utenti`
--
DELIMITER $$
CREATE TRIGGER `trg_utenti_log_ins` BEFORE INSERT ON `utenti` FOR EACH ROW BEGIN
  INSERT INTO storico_operazioni (nome_op)
  VALUES (CONCAT('Registrazione utente: ', NEW.username));
END
$$
DELIMITER ;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `log_operazioni`
--
ALTER TABLE `log_operazioni`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `storico_operazioni`
--
ALTER TABLE `storico_operazioni`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_username` (`username`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `log_operazioni`
--
ALTER TABLE `log_operazioni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `storico_operazioni`
--
ALTER TABLE `storico_operazioni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `utenti`
--
ALTER TABLE `utenti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
