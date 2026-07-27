-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Lug 27, 2026 alle 15:16
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
-- Database: `gensapp`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `messaggi`
--

CREATE TABLE `messaggi` (
  `id` int(11) NOT NULL,
  `messaggio` varbinary(255) NOT NULL,
  `mittente_id` int(11) NOT NULL,
  `destinatario_id` int(11) NOT NULL,
  `ora_invio` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `messaggi`
--

INSERT INTO `messaggi` (`id`, `messaggio`, `mittente_id`, `destinatario_id`, `ora_invio`) VALUES
(1, 0x4369616f21, 1, 2, '2026-07-27 14:52:09'),
(2, 0x456869206369616f21, 2, 1, '2026-07-27 14:52:15'),
(3, 0x436f7361206661636369616d6f20646f706f3f, 1, 2, '2026-07-27 14:52:24'),
(4, 0x6369616f6c6f6c, 3, 1, '2026-07-27 14:57:21'),
(5, 0x656869, 2, 3, '2026-07-27 14:57:29'),
(6, 0x6c6f6c, 2, 4, '2026-07-27 14:57:36'),
(7, 0x6f6b, 1, 2, '2026-07-27 14:57:49'),
(8, 0x686f6c61, 1, 4, '2026-07-27 15:14:10');

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE `utenti` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`id`, `username`) VALUES
(3, 'chiara'),
(2, 'luca'),
(1, 'mario'),
(4, 'martina');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `messaggi`
--
ALTER TABLE `messaggi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mittente_id` (`mittente_id`),
  ADD KEY `destinatario_id` (`destinatario_id`);

--
-- Indici per le tabelle `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `messaggi`
--
ALTER TABLE `messaggi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT per la tabella `utenti`
--
ALTER TABLE `utenti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `messaggi`
--
ALTER TABLE `messaggi`
  ADD CONSTRAINT `messaggi_ibfk_1` FOREIGN KEY (`mittente_id`) REFERENCES `utenti` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `messaggi_ibfk_2` FOREIGN KEY (`destinatario_id`) REFERENCES `utenti` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
