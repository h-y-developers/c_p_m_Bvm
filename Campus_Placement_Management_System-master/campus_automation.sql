-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2021 at 10:40 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `campus_automation`
--

-- --------------------------------------------------------

--
-- Table structure for table `achievements`
--

CREATE TABLE `achievements` (
  `id` int(255) NOT NULL,
  `achieve_id` varchar(255) NOT NULL,
  `achieve_name` mediumtext NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `field_name` varchar(30) NOT NULL,
  `company_name` varchar(30) NOT NULL,
  `issue_date` date NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(4) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mobile_no` int(10) NOT NULL,
  `email_id` varchar(10) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `assignments`
--

CREATE TABLE `assignments` (
  `id` int(255) NOT NULL,
  `assignment_id` varchar(20) NOT NULL,
  `faculty_id` varchar(20) NOT NULL,
  `subject_id` varchar(20) NOT NULL,
  `dept_id` int(10) NOT NULL,
  `issue_date` date NOT NULL,
  `due_date` date NOT NULL,
  `source` varchar(100) NOT NULL,
  `visible_not` enum('yes','no') NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `assignment_record`
--

CREATE TABLE `assignment_record` (
  `id` int(255) NOT NULL,
  `assignment_id` int(255) NOT NULL,
  `faculty_id` varchar(20) NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `subject_id` varchar(20) NOT NULL,
  `upload_date` date NOT NULL,
  `due_date` date NOT NULL,
  `status` enum('pending','fail','success') NOT NULL,
  `rating_star` int(10) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `college`
--

CREATE TABLE `college` (
  `index_no` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `university` varchar(12) NOT NULL,
  `city` varchar(12) NOT NULL,
  `address` longtext NOT NULL,
  `email_id` int(20) NOT NULL,
  `helpline_no` int(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

CREATE TABLE `companies` (
  `company_id` int(50) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `coming_date` date NOT NULL,
  `job_description` longtext NOT NULL,
  `required_student` int(100) NOT NULL DEFAULT '0',
  `no_of_placed_students` int(100) NOT NULL DEFAULT '0',
  `email_id` varchar(15) NOT NULL,
  `field_name` varchar(200) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `college_name` varchar(100) NOT NULL,
  `dept_id` int(10) NOT NULL,
  `dept_name` varchar(50) NOT NULL,
  `dept_hod` varchar(100) NOT NULL,
  `no_of_faculty` int(100) NOT NULL,
  `est_year` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `faculties`
--

CREATE TABLE `faculties` (
  `id` int(255) NOT NULL,
  `id_no` varchar(30) NOT NULL,
  `faculty_name` varchar(200) NOT NULL,
  `mobile_no` varchar(12) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `date_join` date NOT NULL,
  `dept_id` int(10) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `materials`
--

CREATE TABLE `materials` (
  `id` int(255) NOT NULL,
  `material_id` varchar(20) NOT NULL,
  `subject_id` varchar(20) NOT NULL,
  `faculty_id` varchar(20) NOT NULL,
  `ref_name` varchar(100) NOT NULL,
  `source` varchar(255) NOT NULL,
  `upload_date` date NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `placement_rounds`
--

CREATE TABLE `placement_rounds` (
  `round_id` int(255) NOT NULL,
  `round_no` int(5) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `student_id` varchar(100) NOT NULL,
  `dept_name` varchar(50) NOT NULL,
  `round_date` date NOT NULL,
  `status` enum('pending','fail','pass','') NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(255) NOT NULL,
  `project_id` varchar(20) NOT NULL,
  `faculty_id` varchar(20) NOT NULL,
  `subject_id` varchar(20) NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `defination` mediumtext NOT NULL,
  `project_sem` int(10) NOT NULL,
  `project_year` year(4) NOT NULL,
  `source` varchar(255) NOT NULL,
  `due_date` date NOT NULL,
  `rating_star` int(10) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(255) NOT NULL,
  `id_no` varchar(100) NOT NULL,
  `enroll_no` int(100) NOT NULL,
  `mobile_no` varchar(100) NOT NULL,
  `email_id` varchar(40) NOT NULL,
  `student_name` varchar(100) NOT NULL,
  `city` varchar(15) NOT NULL,
  `residential_addr` mediumtext NOT NULL,
  `permanant_addr` mediumtext NOT NULL,
  `ssc_marks` varchar(20) NOT NULL,
  `hsc_marks` varchar(20) NOT NULL,
  `dept_id` int(15) NOT NULL,
  `batch_id` varchar(5) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` int(255) NOT NULL,
  `subject_id` varchar(20) NOT NULL,
  `sub_name` varchar(100) NOT NULL,
  `semester` int(10) NOT NULL,
  `teach_year` year(4) NOT NULL,
  `faculty_id` varchar(20) NOT NULL,
  `dept_id` int(10) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE `timetable` (
  `id` int(255) NOT NULL,
  `time_id` varchar(255) NOT NULL,
  `semester` int(10) NOT NULL,
  `year` year(4) NOT NULL,
  `time` varchar(100) NOT NULL,
  `faculty_name` varchar(100) NOT NULL,
  `type` enum('lab','lecture') NOT NULL,
  `subject_name` varchar(100) NOT NULL,
  `batch_id` varchar(5) NOT NULL,
  `college_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `id` int(255) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `email_id` varchar(30) NOT NULL,
  `type` enum('student','faculty','company') NOT NULL,
  `password` varchar(20) NOT NULL,
  `college_name` varchar(200) NOT NULL,
  `dept_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `assignments`
--
ALTER TABLE `assignments`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `assignment_id` (`assignment_id`);

--
-- Indexes for table `assignment_record`
--
ALTER TABLE `assignment_record`
  ADD PRIMARY KEY (`id`,`assignment_id`);

--
-- Indexes for table `college`
--
ALTER TABLE `college`
  ADD PRIMARY KEY (`index_no`,`name`);

--
-- Indexes for table `companies`
--
ALTER TABLE `companies`
  ADD PRIMARY KEY (`company_id`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD UNIQUE KEY `dept_id` (`dept_id`);

--
-- Indexes for table `faculties`
--
ALTER TABLE `faculties`
  ADD PRIMARY KEY (`id`,`id_no`);

--
-- Indexes for table `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `placement_rounds`
--
ALTER TABLE `placement_rounds`
  ADD PRIMARY KEY (`round_id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`,`id_no`,`enroll_no`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`,`subject_id`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`id`,`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assignments`
--
ALTER TABLE `assignments`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `assignment_record`
--
ALTER TABLE `assignment_record`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `companies`
--
ALTER TABLE `companies`
  MODIFY `company_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `faculties`
--
ALTER TABLE `faculties`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `materials`
--
ALTER TABLE `materials`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `placement_rounds`
--
ALTER TABLE `placement_rounds`
  MODIFY `round_id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_info`
--
ALTER TABLE `user_info`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
