CREATE DATABASE  IF NOT EXISTS `system_audit` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `system_audit`;
-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (i686)
--
-- Host: 127.0.0.1    Database: system_audit
-- ------------------------------------------------------
-- Server version	5.5.46-0ubuntu0.14.04.2-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `audit_audit_track`
--

DROP TABLE IF EXISTS `audit_audit_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_audit_track` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unused_program` varchar(200) DEFAULT NULL,
  `clean_temp` varchar(200) DEFAULT NULL,
  `antivirus` varchar(200) DEFAULT NULL,
  `server_check` varchar(200) DEFAULT NULL,
  `connectivity_check` varchar(200) DEFAULT NULL,
  `printer_check` varchar(200) DEFAULT NULL,
  `issue` varchar(200) DEFAULT NULL,
  `email_backup` datetime DEFAULT NULL,
  `audit_entry` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `audit_audit_track_user_id_5e9c661d_fk_audit_user_entry_id` (`user_id`),
  CONSTRAINT `audit_audit_track_user_id_5e9c661d_fk_audit_user_entry_id` FOREIGN KEY (`user_id`) REFERENCES `audit_user_entry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_audit_track`
--

LOCK TABLES `audit_audit_track` WRITE;
/*!40000 ALTER TABLE `audit_audit_track` DISABLE KEYS */;
/*!40000 ALTER TABLE `audit_audit_track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_email_details`
--

DROP TABLE IF EXISTS `audit_email_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_email_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email_user_name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_email_details`
--

LOCK TABLES `audit_email_details` WRITE;
/*!40000 ALTER TABLE `audit_email_details` DISABLE KEYS */;
INSERT INTO `audit_email_details` VALUES (1,'bossops@bluewatertradewinds.onmicrosoft.com'),(2,'ankit@bluewatertradewinds.onmicrosoft.com'),(3,'team@bluewatertradewinds.onmicrosoft.com');
/*!40000 ALTER TABLE `audit_email_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_register_details`
--

DROP TABLE IF EXISTS `audit_register_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_register_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_date` date DEFAULT NULL,
  `it_non` varchar(20) DEFAULT NULL,
  `fitting` varchar(20) DEFAULT NULL,
  `description` varchar(20) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `user_allotted` varchar(20) DEFAULT NULL,
  `security_level` varchar(20) DEFAULT NULL,
  `maintenance` varchar(20) DEFAULT NULL,
  `record_date` date DEFAULT NULL,
  `remarks` varchar(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `audit_key` varchar(100),
  PRIMARY KEY (`id`),
  KEY `audit_register_details_user_id_6219efbf_fk_audit_user_entry_id` (`user_id`),
  CONSTRAINT `audit_register_details_user_id_6219efbf_fk_audit_user_entry_id` FOREIGN KEY (`user_id`) REFERENCES `audit_user_entry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_register_details`
--

LOCK TABLES `audit_register_details` WRITE;
/*!40000 ALTER TABLE `audit_register_details` DISABLE KEYS */;
INSERT INTO `audit_register_details` VALUES (1,NULL,'Operation','Peripheral','CPU,Keyboard,Mouse,U','Operation','ANURAG TIWARI-PC','3- Medium','Weekly','2019-10-02','',6,'BW/CPU/001'),(2,NULL,'Operation','Peripheral','CPU,Keyboard,Mouse,U','Operation','SUHAIL GURUNG-PC','3- Medium','Weekly','2019-10-02','',7,'BW/CPU/002'),(4,NULL,'Operation','Peripheral','CPU,Keyboard,Mouse,U','Operation','RAJENDRA PRASAD-PC','3- Medium','Weekly','2019-10-02','',8,'BW/CPU/003'),(6,NULL,'IT Room','Peripheral','CPU,Keyboard,Mouse,U','IT Room','ADITYA SAHI-PC','3- Medium','Weekly','2019-10-02','',9,'BW/CPU/004'),(8,NULL,'IT Room','Peripheral','CPU,Keyboard,Mouse,U','IT Room','ETHERM-PC','3- Medium','Weekly','2019-10-02','',10,'BW/CPU/005'),(10,NULL,'Operation','Peripheral','CPU,Keyboard,Mouse,U','Operation','SACHIN GUPTA-PC','3- Medium','Weekly','2019-10-02','',11,'BW/CPU/006'),(12,NULL,'Operation','Peripheral','CPU,Keyboard,Mouse,U','Operation','SANTOSH TIWARI-PC','3- Medium','Weekly','2019-10-02','',12,'BW/CPU/007'),(14,NULL,'IT Room','Peripheral','CPU,Keyboard,Mouse,U','IT Room','SANDEEP-PC','3- Medium','Weekly','2019-10-02','',13,'BW/CPU/008');
/*!40000 ALTER TABLE `audit_register_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_remainder_details`
--

DROP TABLE IF EXISTS `audit_remainder_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_remainder_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remainder_date` date DEFAULT NULL,
  `office_period_date` varchar(20) DEFAULT NULL,
  `email_move_date` varchar(20) DEFAULT NULL,
  `remarks` varchar(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `audit_remainder_details_user_id_7bb95d8e_fk_audit_user_entry_id` (`user_id`),
  CONSTRAINT `audit_remainder_details_user_id_7bb95d8e_fk_audit_user_entry_id` FOREIGN KEY (`user_id`) REFERENCES `audit_user_entry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_remainder_details`
--

LOCK TABLES `audit_remainder_details` WRITE;
/*!40000 ALTER TABLE `audit_remainder_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `audit_remainder_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_user_entry`
--

DROP TABLE IF EXISTS `audit_user_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_user_entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(200) DEFAULT NULL,
  `hdd` varchar(200) DEFAULT NULL,
  `processor` varchar(200) DEFAULT NULL,
  `ram` varchar(200) DEFAULT NULL,
  `operating_sys` varchar(200),
  `remark` varchar(200),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_user_entry`
--

LOCK TABLES `audit_user_entry` WRITE;
/*!40000 ALTER TABLE `audit_user_entry` DISABLE KEYS */;
INSERT INTO `audit_user_entry` VALUES (6,'ANURAG TIWARI-PC','   320','i3','4 GB','Windows 7 Professional ','   No'),(7,'SUHAIL GURUNG-PC',' 320','i3','4 GB',' Windows 7 Professional',' No'),(8,'RAJENDRA PRASAD-PC','','','','',''),(9,'ADITYA SAHI-PC','','','','',''),(10,'ETHERM-PC','','','','',''),(11,'SACHIN GUPTA-PC','','','','',''),(12,'SANTOSH TIWARI-PC','','','','',''),(13,'SANDEEP-PC','','','','',''),(14,'LOKESH BHATT-PC','','','','',''),(15,'MANJEET NEGI-PC','','','','',''),(16,'ANKIT UNIYAL-PC','','','','',''),(17,'VIKASH RAWAT-PC','','','','',''),(18,'UDIT KHANDURI-PC','','','','',''),(19,'SERVER-PC','','','','',''),(20,'SHUBHAM VERMA-PC','','','','',''),(21,'ANKIT MITTAL-PC','','','','',''),(22,'APURAV SAKLANI-PC','','','','',''),(23,'ABHISHEK BAIRWAN-PC','320 ','i4','4 GB',' Windows 7 Professional',' No'),(24,'SOBHIT RAWAT-PC','','','','',''),(25,'AMIT UNIYAL-PC','','','','',''),(26,'YUVRAJ-PC','','','','',''),(27,'RAHUL NEGI-PC','','','','',''),(28,'NARANYAN-PC','','','','',''),(29,'VARUN-PC','','','','',''),(30,'UPDESH-PC','','','','','');
/*!40000 ALTER TABLE `audit_user_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_weekly_entry`
--

DROP TABLE IF EXISTS `audit_weekly_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_weekly_entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `boot_time` varchar(20) DEFAULT NULL,
  `unused_program` varchar(20) DEFAULT NULL,
  `temp_file` varchar(20) DEFAULT NULL,
  `up_antivirus` varchar(20) DEFAULT NULL,
  `history_clean` varchar(20) DEFAULT NULL,
  `server_folder` varchar(20) DEFAULT NULL,
  `internet_conn` varchar(20) DEFAULT NULL,
  `printer_conn` varchar(20) DEFAULT NULL,
  `issue_any` varchar(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `audit_weekly_entry_user_id_519a8753_fk_audit_user_entry_id` (`user_id`),
  CONSTRAINT `audit_weekly_entry_user_id_519a8753_fk_audit_user_entry_id` FOREIGN KEY (`user_id`) REFERENCES `audit_user_entry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_weekly_entry`
--

LOCK TABLES `audit_weekly_entry` WRITE;
/*!40000 ALTER TABLE `audit_weekly_entry` DISABLE KEYS */;
INSERT INTO `audit_weekly_entry` VALUES (1,'25 sec','YES','YES',NULL,'YES',NULL,'YES','YES','No',23,'2019-10-03'),(2,'32 sec','YES','YES',NULL,'YES',NULL,'YES','YES','No',7,'2019-10-03');
/*!40000 ALTER TABLE `audit_weekly_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user_entry',7,'add_user_entry'),(20,'Can change user_entry',7,'change_user_entry'),(21,'Can delete user_entry',7,'delete_user_entry'),(22,'Can add weekly_entry',8,'add_weekly_entry'),(23,'Can change weekly_entry',8,'change_weekly_entry'),(24,'Can delete weekly_entry',8,'delete_weekly_entry'),(25,'Can add email_details',9,'add_email_details'),(26,'Can change email_details',9,'change_email_details'),(27,'Can delete email_details',9,'delete_email_details'),(28,'Can add remainder_details',10,'add_remainder_details'),(29,'Can change remainder_details',10,'change_remainder_details'),(30,'Can delete remainder_details',10,'delete_remainder_details'),(31,'Can add register_details',11,'add_register_details'),(32,'Can change register_details',11,'change_register_details'),(33,'Can delete register_details',11,'delete_register_details');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'audit','email_details'),(11,'audit','register_details'),(10,'audit','remainder_details'),(7,'audit','user_entry'),(8,'audit','weekly_entry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-01-31 16:45:35'),(2,'auth','0001_initial','2018-01-31 16:45:37'),(3,'admin','0001_initial','2018-01-31 16:45:37'),(4,'audit','0001_initial','2018-01-31 16:45:38'),(5,'contenttypes','0002_remove_content_type_name','2018-01-31 16:45:38'),(6,'auth','0002_alter_permission_name_max_length','2018-01-31 16:45:38'),(7,'auth','0003_alter_user_email_max_length','2018-01-31 16:45:39'),(8,'auth','0004_alter_user_username_opts','2018-01-31 16:45:39'),(9,'auth','0005_alter_user_last_login_null','2018-01-31 16:45:39'),(10,'auth','0006_require_contenttypes_0002','2018-01-31 16:45:39'),(11,'sessions','0001_initial','2018-01-31 16:45:39'),(12,'audit','0002_auto_20190822_1641','2019-08-22 16:41:14'),(13,'audit','0003_weekly_entry','2019-08-22 16:57:18'),(14,'audit','0002_weekly_entry_entry_date','2019-08-22 17:30:38'),(15,'audit','0002_email_details','2019-10-01 05:04:34'),(16,'audit','0003_auto_20191001_1054','2019-10-01 10:54:27'),(17,'audit','0004_remainder_details','2019-10-01 12:38:00'),(18,'audit','0005_register_details','2019-10-02 09:11:14'),(19,'audit','0006_register_details_audit_key','2019-10-02 09:26:16');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-04 18:13:09
