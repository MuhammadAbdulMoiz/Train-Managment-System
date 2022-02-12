-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 12, 2022 at 01:28 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qasier's train`
--
CREATE DATABASE IF NOT EXISTS `qasier's train` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `qasier's train`;

-- --------------------------------------------------------

--
-- Table structure for table `passenger_detail`
--

DROP TABLE IF EXISTS `passenger_detail`;
CREATE TABLE IF NOT EXISTS `passenger_detail` (
  `name` varchar(40) NOT NULL,
  `age` int NOT NULL,
  `CNIC` bigint NOT NULL,
  `date` date NOT NULL,
  `booking_class` varchar(40) NOT NULL,
  `departure` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `destination` varchar(40) NOT NULL,
  `ticket_id` int NOT NULL AUTO_INCREMENT,
  `timing` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `fare` int NOT NULL,
  PRIMARY KEY (`ticket_id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `passenger_detail`
--

INSERT INTO `passenger_detail` (`name`, `age`, `CNIC`, `date`, `booking_class`, `departure`, `destination`, `ticket_id`, `timing`, `fare`) VALUES
('Abdul Moiz', 18, 6110121132845, '2022-02-12', 'Economy', 'Lahore', 'Quetta', 42, 'Departure : 12AM     Destination : 5PM', 640);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
