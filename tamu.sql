-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Waktu pembuatan: 01 Jan 2021 pada 17.18
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tamu`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tamu_masuk`
--

CREATE TABLE `tamu_masuk` (
  `id` int(20) NOT NULL,
  `nama_tamu` varchar(50) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `keperluan` varchar(200) NOT NULL,
  `jam_masuk` datetime NOT NULL,
  `jam_keluar` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tamu_masuk`
--

INSERT INTO `tamu_masuk` (`id`, `nama_tamu`, `alamat`, `keperluan`, `jam_masuk`, `jam_keluar`) VALUES
(9, 'sumadi', 'Brajan', 'beli Seblak', '2021-01-01 22:41:07', '2021-01-01 22:41:07');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tamu_masuk`
--
ALTER TABLE `tamu_masuk`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `tamu_masuk`
--
ALTER TABLE `tamu_masuk`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
