-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Jun 27, 2022 at 12:34 AM
-- Server version: 10.6.7-MariaDB-1:10.6.7+maria~focal
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy_gsp_app`
--
CREATE DATABASE IF NOT EXISTS `pharmacy_gsp_app` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `pharmacy_gsp_app`;

-- --------------------------------------------------------

--
-- Table structure for table `obat`
--

DROP TABLE IF EXISTS `obat`;
CREATE TABLE `obat` (
  `id` bigint(20) NOT NULL,
  `kode_produk` varchar(100) DEFAULT NULL,
  `nama_produk` varchar(100) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `uuid` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `obat`
--

INSERT INTO `obat` (`id`, `kode_produk`, `nama_produk`, `jumlah`, `uuid`) VALUES
(99844800626294784, 'A001', 'Amoxcilin', 100, '74b1479f-93f8-43d0-9382-a87870682d52'),
(99844800626294785, 'A002', 'Detrometrophan', 110, '60b360ef-2b80-4c7f-a1b0-269defd8a33b'),
(99844800626294786, 'A003', 'Paracetamol', 120, 'd89541da-9c87-4a9d-8807-a0438d54bcc2');

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

DROP TABLE IF EXISTS `pengguna`;
CREATE TABLE `pengguna` (
  `id` bigint(20) NOT NULL,
  `nama_pengguna` varchar(100) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `uuid` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id`, `nama_pengguna`, `role`, `username`, `password`, `uuid`) VALUES
(99844800626294787, 'Petugas 1', 'Administrator', 'admin', 'admin', '984a700c-4162-44d0-9afd-b98b3f8c095e');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

DROP TABLE IF EXISTS `transaksi`;
CREATE TABLE `transaksi` (
  `id` bigint(20) NOT NULL,
  `nomor_transaksi` varchar(100) DEFAULT NULL,
  `tanggal_transaksi` datetime DEFAULT NULL,
  `nama_pelanggan` varchar(100) DEFAULT NULL,
  `uuid` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id`, `nomor_transaksi`, `tanggal_transaksi`, `nama_pelanggan`, `uuid`) VALUES
(99845312599818240, 'TRN-001', '2021-10-10 08:00:00', 'Ibnu', 'fbbe49fa-043f-44f7-b97c-dad02f45bb60');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_item`
--

DROP TABLE IF EXISTS `transaksi_item`;
CREATE TABLE `transaksi_item` (
  `id` bigint(20) NOT NULL,
  `id_transaksi` bigint(20) DEFAULT NULL,
  `id_produk` varchar(100) DEFAULT NULL,
  `kode_produk` varchar(100) DEFAULT NULL,
  `nama_produk` varchar(100) DEFAULT NULL,
  `jumlah_produk` int(11) DEFAULT NULL,
  `uuid` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaksi_item`
--

INSERT INTO `transaksi_item` (`id`, `id_transaksi`, `id_produk`, `kode_produk`, `nama_produk`, `jumlah_produk`, `uuid`) VALUES
(99845312599818241, 99845312599818240, '99844800626294784', 'A001', 'Amoxcilin', 1, '48af5954-bfdd-43d3-a622-0b101bdc59fb'),
(99845312599818242, 99845312599818240, '99844800626294784', 'A001', 'Amoxcilin', 1, '3b48f2ac-0448-4761-957e-65a3b6c1d797'),
(99845312599818243, 99845312599818240, '99844800626294785', 'A002', 'Detrometrophan', 5, 'c6426ff5-490c-40fa-89fa-e97c850ff7d9'),
(99845312599818244, 99845312599818240, '99844800626294786', 'A003', 'Paracetamol', 4, '0db132b0-cd09-4d9d-a164-6acaace1785c');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `obat`
--
ALTER TABLE `obat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_produk` (`kode_produk`),
  ADD UNIQUE KEY `uuid` (`uuid`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `password` (`password`),
  ADD UNIQUE KEY `uuid` (`uuid`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uuid` (`uuid`);

--
-- Indexes for table `transaksi_item`
--
ALTER TABLE `transaksi_item`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uuid` (`uuid`),
  ADD KEY `id_transaksi` (`id_transaksi`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaksi_item`
--
ALTER TABLE `transaksi_item`
  ADD CONSTRAINT `transaksi_item_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `transaksi` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
