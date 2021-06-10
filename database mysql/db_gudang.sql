-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 01, 2021 at 05:52 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_gudang`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(7) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama`, `username`, `password`) VALUES
(1, 'iqbal riyadi', 'iqbal', '123'),
(2, 'dymasalfin', 'alfinn', '123');

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id_barang` int(11) NOT NULL,
  `jenis_barang` varchar(20) NOT NULL,
  `merk` varchar(20) NOT NULL,
  `warna` varchar(20) NOT NULL,
  `ukuran` varchar(5) NOT NULL,
  `jumlahstok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id_barang`, `jenis_barang`, `merk`, `warna`, `ukuran`, `jumlahstok`) VALUES
(2, 'kaos', 'crooz', 'hijau', 'L', 7),
(5, 'kaos', '3second', 'putih', 'L', 11),
(6, 'kaos', 'crooz', 'putih', 'L', 3),
(7, 'kaos', '3second', 'hitam', 'L', 2),
(8, 'kaos', 'crooz', 'hijau', 'XL', 2),
(9, 'celana', 'levis', 'hitam', '26', 5),
(10, 'celana', 'levis', 'biru', '30', 3),
(14, 'topi', 'crooz', 'hitam', 'M', 10),
(15, 'sepatu', 'vans', 'hitam putih', '32', 1),
(16, 'sepatu', 'kompas', 'merah', '30', 4),
(17, 'topi', 'deus', 'hitam', 'L', 3),
(19, 'kaos', 'deus', 'hitam', 'XL', 1),
(20, 'sepatu', 'kompas 2002', 'hitam', '32', 1),
(21, 'sepatu', 'kompas 2002', 'merah putih', '40', 1),
(22, 'sepatu', 'vans', 'hitam putih', '42', 4),
(24, 'sepatu', 'vans', 'hitam', '40', 4);

-- --------------------------------------------------------

--
-- Table structure for table `detail_transaksi`
--

CREATE TABLE `detail_transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_barang` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `masuk/keluar` varchar(11) NOT NULL,
  `tanggal` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detail_transaksi`
--

INSERT INTO `detail_transaksi` (`id_transaksi`, `id_barang`, `jumlah`, `masuk/keluar`, `tanggal`) VALUES
(1, 22, 5, 'masuk', '2021-01-01 23:00:54'),
(2, 22, 2, 'keluar', '2021-01-01 23:46:02'),
(3, 24, 5, 'masuk', '2021-01-01 23:48:21'),
(4, 24, 2, 'keluar', '2021-01-01 23:49:07'),
(5, 17, 2, 'masuk', '2021-01-01 23:50:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`id_barang`);

--
-- Indexes for table `detail_transaksi`
--
ALTER TABLE `detail_transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_barang` (`id_barang`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `id_barang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `detail_transaksi`
--
ALTER TABLE `detail_transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detail_transaksi`
--
ALTER TABLE `detail_transaksi`
  ADD CONSTRAINT `detail_transaksi_ibfk_1` FOREIGN KEY (`id_barang`) REFERENCES `barang` (`id_barang`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
