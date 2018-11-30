-- MySQL dump 10.13  Distrib 5.7.21, for macos10.13 (x86_64)
--
-- Host: localhost    Database: clinical
-- ------------------------------------------------------
-- Server version	5.7.21

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add application',6,'add_application'),(17,'Can change application',6,'change_application'),(18,'Can delete application',6,'delete_application'),(19,'Can add access token',7,'add_accesstoken'),(20,'Can change access token',7,'change_accesstoken'),(21,'Can delete access token',7,'delete_accesstoken'),(22,'Can add grant',8,'add_grant'),(23,'Can change grant',8,'change_grant'),(24,'Can delete grant',8,'delete_grant'),(25,'Can add refresh token',9,'add_refreshtoken'),(26,'Can change refresh token',9,'change_refreshtoken'),(27,'Can delete refresh token',9,'delete_refreshtoken'),(28,'Can add cors model',10,'add_corsmodel'),(29,'Can change cors model',10,'change_corsmodel'),(30,'Can delete cors model',10,'delete_corsmodel'),(31,'Can add 临床诊断',11,'add_clinicalconclusion'),(32,'Can change 临床诊断',11,'change_clinicalconclusion'),(33,'Can delete 临床诊断',11,'delete_clinicalconclusion'),(34,'Can add 基本信息',12,'add_generalinfo'),(35,'Can change 基本信息',12,'change_generalinfo'),(36,'Can delete 基本信息',12,'delete_generalinfo'),(37,'prj001_all_permissions',12,'prj001_operation'),(38,'Can add 上传文件',13,'add_investfileupload'),(39,'Can change 上传文件',13,'change_investfileupload'),(40,'Can delete 上传文件',13,'delete_investfileupload'),(41,'Can add 月经情况',14,'add_menstruation'),(42,'Can change 月经情况',14,'change_menstruation'),(43,'Can delete 月经情况',14,'delete_menstruation'),(44,'Can add 其它情况',15,'add_other'),(45,'Can change 其它情况',15,'change_other'),(46,'Can delete 其它情况',15,'delete_other'),(47,'Can add 全身症状',16,'add_symptom'),(48,'Can change 全身症状',16,'change_symptom'),(49,'Can delete 全身症状',16,'delete_symptom'),(50,'Can add 用户信息',17,'add_myuser'),(51,'Can change 用户信息',17,'change_myuser'),(52,'Can delete 用户信息',17,'delete_myuser'),(53,'user_all_permissions',17,'user_operation'),(54,'Can add 流调项目',18,'add_clinicalprojects'),(55,'Can change 流调项目',18,'change_clinicalprojects'),(56,'Can delete 流调项目',18,'delete_clinicalprojects');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_myusers_myuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_myusers_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
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
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(10,'corsheaders','corsmodel'),(17,'myusers','myuser'),(7,'oauth2_provider','accesstoken'),(6,'oauth2_provider','application'),(8,'oauth2_provider','grant'),(9,'oauth2_provider','refreshtoken'),(11,'prj001','clinicalconclusion'),(12,'prj001','generalinfo'),(13,'prj001','investfileupload'),(14,'prj001','menstruation'),(15,'prj001','other'),(16,'prj001','symptom'),(18,'projects','clinicalprojects'),(5,'sessions','session');
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
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-27 06:46:09.242254'),(2,'contenttypes','0002_remove_content_type_name','2018-11-27 06:46:09.318226'),(3,'auth','0001_initial','2018-11-27 06:46:09.550462'),(4,'auth','0002_alter_permission_name_max_length','2018-11-27 06:46:09.585993'),(5,'auth','0003_alter_user_email_max_length','2018-11-27 06:46:09.593046'),(6,'auth','0004_alter_user_username_opts','2018-11-27 06:46:09.599464'),(7,'auth','0005_alter_user_last_login_null','2018-11-27 06:46:09.608779'),(8,'auth','0006_require_contenttypes_0002','2018-11-27 06:46:09.612304'),(9,'auth','0007_alter_validators_add_error_messages','2018-11-27 06:46:09.618933'),(10,'auth','0008_alter_user_username_max_length','2018-11-27 06:46:09.630062'),(11,'auth','0009_alter_user_last_name_max_length','2018-11-27 06:46:09.642417'),(12,'myusers','0001_initial','2018-11-27 06:46:09.866362'),(13,'admin','0001_initial','2018-11-27 06:46:09.958545'),(14,'admin','0002_logentry_remove_auto_add','2018-11-27 06:46:09.969559'),(15,'oauth2_provider','0001_initial','2018-11-27 06:46:10.398887'),(16,'oauth2_provider','0002_08_updates','2018-11-27 06:46:10.601827'),(17,'oauth2_provider','0003_auto_20160316_1503','2018-11-27 06:46:10.683857'),(18,'oauth2_provider','0004_auto_20160525_1623','2018-11-27 06:46:10.862652'),(19,'oauth2_provider','0005_auto_20170514_1141','2018-11-27 06:46:12.008324'),(20,'oauth2_provider','0006_auto_20171214_2232','2018-11-27 06:46:12.258134'),(21,'prj001','0001_initial','2018-11-27 06:46:13.052995'),(22,'projects','0001_initial','2018-11-27 06:46:13.223026'),(23,'sessions','0001_initial','2018-11-27 06:46:13.271844'),(24,'prj001','0002_auto_20181129_1522','2018-11-29 07:22:48.681254'),(25,'prj001','0003_auto_20181129_1716','2018-11-29 09:16:37.263945'),(26,'prj001','0004_auto_20181129_1717','2018-11-29 09:17:39.854489');
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('99qxzypw827iu3j53tjxwhxjhgym9x5i','ZTk2NzQ5NTU2NDhiODZmMWI5ODFiNGYzZTQyYzc2MmQ0NGZlZjgxZTp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzlmODc4YTZkZDA4ZGM5MjY5NmM4YjdiOTM2NDYwYjgyYTA2Y2RmNSJ9','2018-12-14 05:50:59.776030'),('mhksectzw8li20d32ykf4hlz4westy2w','ZjgyNzQxOTM4NTBlNjEwOGY1YmUyMjhlZmNjNzY3ZDI2MGVjOGRjODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNWQyZmY1ZTI1MTI3OTFiNmFlYzYzYzY5YmM5MjRjZmE5MGE5Y2QwIn0=','2018-12-11 12:53:57.474965');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myusers_myuser`
--

DROP TABLE IF EXISTS `myusers_myuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myusers_myuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `hospital` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myusers_myuser`
--

LOCK TABLES `myusers_myuser` WRITE;
/*!40000 ALTER TABLE `myusers_myuser` DISABLE KEYS */;
INSERT INTO `myusers_myuser` VALUES (13,'pbkdf2_sha256$100000$gx6dly2ITBc1$VdTBbwfUp/A1MyskRqiyl6Xam0qpfVzyzalg91fbV5w=','2018-11-30 05:50:59.771544',1,'1@163.com','17630975001','wo','','',1,1),(14,'pbkdf2_sha256$100000$gpnST1rMqxep$kPYL/KQI6XB9AhLUzFB57k283asxlYxxKSe5688jg64=',NULL,0,'yinzhonghua@handian.com','17630975002','hua111','','',1,0);
/*!40000 ALTER TABLE `myusers_myuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myusers_myuser_groups`
--

DROP TABLE IF EXISTS `myusers_myuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myusers_myuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myusers_myuser_groups_myuser_id_group_id_9a93819b_uniq` (`myuser_id`,`group_id`),
  KEY `myusers_myuser_groups_group_id_64e86638_fk_auth_group_id` (`group_id`),
  CONSTRAINT `myusers_myuser_groups_group_id_64e86638_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `myusers_myuser_groups_myuser_id_9af25087_fk_myusers_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myusers_myuser_groups`
--

LOCK TABLES `myusers_myuser_groups` WRITE;
/*!40000 ALTER TABLE `myusers_myuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `myusers_myuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myusers_myuser_user_permissions`
--

DROP TABLE IF EXISTS `myusers_myuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myusers_myuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myusers_myuser_user_perm_myuser_id_permission_id_3cae80a2_uniq` (`myuser_id`,`permission_id`),
  KEY `myusers_myuser_user__permission_id_a5ec36bd_fk_auth_perm` (`permission_id`),
  CONSTRAINT `myusers_myuser_user__myuser_id_aed2ffb5_fk_myusers_m` FOREIGN KEY (`myuser_id`) REFERENCES `myusers_myuser` (`id`),
  CONSTRAINT `myusers_myuser_user__permission_id_a5ec36bd_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myusers_myuser_user_permissions`
--

LOCK TABLES `myusers_myuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `myusers_myuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `myusers_myuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `source_refresh_token_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_accesstoken_token_8af090f8_uniq` (`token`),
  UNIQUE KEY `source_refresh_token_id` (`source_refresh_token_id`),
  KEY `oauth2_provider_acce_user_id_6e4c9a65_fk_myusers_m` (`user_id`),
  KEY `oauth2_provider_accesstoken_application_id_b22886e1_fk` (`application_id`),
  CONSTRAINT `oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr` FOREIGN KEY (`source_refresh_token_id`) REFERENCES `oauth2_provider_refreshtoken` (`id`),
  CONSTRAINT `oauth2_provider_acce_user_id_6e4c9a65_fk_myusers_m` FOREIGN KEY (`user_id`) REFERENCES `myusers_myuser` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_application_id_b22886e1_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_accesstoken` VALUES (21,'DePjNKrB2ux8IrfUTdyyV1j9YqjWE8','2018-11-30 13:55:31.723935','prj001 prj002 users',3,14,'2018-11-30 05:55:31.724361','2018-11-30 05:55:31.724377',NULL);
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_application` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) NOT NULL,
  `redirect_uris` longtext NOT NULL,
  `client_type` varchar(32) NOT NULL,
  `authorization_grant_type` varchar(32) NOT NULL,
  `client_secret` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  KEY `oauth2_provider_appl_user_id_79829054_fk_myusers_m` (`user_id`),
  CONSTRAINT `oauth2_provider_appl_user_id_79829054_fk_myusers_m` FOREIGN KEY (`user_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
INSERT INTO `oauth2_provider_application` VALUES (3,'CWrbfzmJOhtG4cF0suVf0rGYSiJDWXeQBWxnne3g','','public','password','REmyfsiy3egeWWy3JF631S2kURtz9QbvdWnhptSx6011I9e1fyttmvZ9r9PiixZvvvcWQlvPFWtKHI9i5HfEVNC6e8a1BhTlfAtzqIa1KJySln3nMbJ4ri0Jkk9PS9x3','clinicalinvest',13,0,'2018-11-30 05:53:33.047408','2018-11-30 05:53:33.047468');
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` varchar(255) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_grant_code_49ab4ddf_uniq` (`code`),
  KEY `oauth2_provider_grant_application_id_81923564_fk` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_myusers_myuser_id` (`user_id`),
  CONSTRAINT `oauth2_provider_grant_application_id_81923564_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_myusers_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `access_token_id` bigint(20) DEFAULT NULL,
  `application_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `revoked` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq` (`token`,`revoked`),
  KEY `oauth2_provider_refreshtoken_application_id_2d1c311b_fk` (`application_id`),
  KEY `oauth2_provider_refr_user_id_da837fce_fk_myusers_m` (`user_id`),
  CONSTRAINT `oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  CONSTRAINT `oauth2_provider_refr_user_id_da837fce_fk_myusers_m` FOREIGN KEY (`user_id`) REFERENCES `myusers_myuser` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_application_id_2d1c311b_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_refreshtoken` VALUES (19,'lna7czFUx3TdCXYhuW3TxXI4Z4ftZT',21,3,14,'2018-11-30 05:55:31.725111','2018-11-30 05:55:31.725135',NULL);
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prj001_clinicalconclusion`
--

DROP TABLE IF EXISTS `prj001_clinicalconclusion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prj001_clinicalconclusion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `benglou` tinyint(1) NOT NULL,
  `yuejingguoduo` tinyint(1) NOT NULL,
  `yuejingxianqi` tinyint(1) NOT NULL,
  `jingqiyanchang` tinyint(1) NOT NULL,
  `jingjianqichuxie` tinyint(1) NOT NULL,
  `shenyin` tinyint(1) NOT NULL,
  `shenyang` tinyint(1) NOT NULL,
  `shenqi` tinyint(1) NOT NULL,
  `piqi` tinyint(1) NOT NULL,
  `qixuxiaxian` tinyint(1) NOT NULL,
  `xure` tinyint(1) NOT NULL,
  `xinpiliangxu` tinyint(1) NOT NULL,
  `pishenyangxu` tinyint(1) NOT NULL,
  `qixuekuixu` tinyint(1) NOT NULL,
  `ganshenyinxu` tinyint(1) NOT NULL,
  `qita_asthenic` varchar(50) NOT NULL,
  `ganyuxuere` tinyint(1) NOT NULL,
  `yangshengxuere` tinyint(1) NOT NULL,
  `ganjingshire` tinyint(1) NOT NULL,
  `tanreyuzu` tinyint(1) NOT NULL,
  `tanshizuzhi` tinyint(1) NOT NULL,
  `tanyuzuzhi` tinyint(1) NOT NULL,
  `yurehujie` tinyint(1) NOT NULL,
  `xueyu` tinyint(1) NOT NULL,
  `qizhixueyu` tinyint(1) NOT NULL,
  `hanningxueyu` tinyint(1) NOT NULL,
  `qita_demonstration` varchar(50) NOT NULL,
  `shenxuxueyu` tinyint(1) NOT NULL,
  `shenxuyure` tinyint(1) NOT NULL,
  `shenxuganyu` tinyint(1) NOT NULL,
  `qixuxueyu` tinyint(1) NOT NULL,
  `yinxuxueyu` tinyint(1) NOT NULL,
  `yinxuhuowang` tinyint(1) NOT NULL,
  `ganyupixu` tinyint(1) NOT NULL,
  `qita_def_ex` varchar(50) NOT NULL,
  `duonangluanchao` tinyint(1) NOT NULL,
  `gaomirusu` tinyint(1) NOT NULL,
  `dicuxingxianjisu` tinyint(1) NOT NULL,
  `qita_west` varchar(50) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  KEY `prj001_clinicalconclusion_owner_id_96864524_fk_myusers_myuser_id` (`owner_id`),
  CONSTRAINT `prj001_clinicalconcl_person_id_d4d69d68_fk_prj001_ge` FOREIGN KEY (`person_id`) REFERENCES `prj001_generalinfo` (`id`),
  CONSTRAINT `prj001_clinicalconclusion_owner_id_96864524_fk_myusers_myuser_id` FOREIGN KEY (`owner_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prj001_clinicalconclusion`
--

LOCK TABLES `prj001_clinicalconclusion` WRITE;
/*!40000 ALTER TABLE `prj001_clinicalconclusion` DISABLE KEYS */;
INSERT INTO `prj001_clinicalconclusion` VALUES (8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,0,1,0,0,0,0,0,0,0,'',0,0,0,0,0,0,0,'',1,0,1,'其他',14,35);
/*!40000 ALTER TABLE `prj001_clinicalconclusion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prj001_generalinfo`
--

DROP TABLE IF EXISTS `prj001_generalinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prj001_generalinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recdate` date NOT NULL,
  `serial` varchar(50) NOT NULL,
  `hospital` varchar(100) NOT NULL,
  `expert` varchar(50) NOT NULL,
  `title` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `weight` decimal(4,1) NOT NULL,
  `blood_type` varchar(10) NOT NULL,
  `nation` varchar(20) NOT NULL,
  `career` varchar(20) NOT NULL,
  `gaokong` tinyint(1) NOT NULL,
  `diwen` tinyint(1) NOT NULL,
  `zaosheng` tinyint(1) NOT NULL,
  `fushe` tinyint(1) NOT NULL,
  `huagongyinran` tinyint(1) NOT NULL,
  `julieyundong` tinyint(1) NOT NULL,
  `qiyou` tinyint(1) NOT NULL,
  `wu` tinyint(1) NOT NULL,
  `address` varchar(100) NOT NULL,
  `entrance` varchar(10) NOT NULL,
  `culture` varchar(30) NOT NULL,
  `marriage` varchar(30) NOT NULL,
  `wuteshu` tinyint(1) NOT NULL,
  `sushi` tinyint(1) NOT NULL,
  `suan` tinyint(1) NOT NULL,
  `tian` tinyint(1) NOT NULL,
  `xian` tinyint(1) NOT NULL,
  `xinla` tinyint(1) NOT NULL,
  `you` tinyint(1) NOT NULL,
  `shengleng` tinyint(1) NOT NULL,
  `kafei` tinyint(1) NOT NULL,
  `qita` varchar(50) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `prj001_generalinfo_owner_id_3383442a_fk_myusers_myuser_id` (`owner_id`),
  CONSTRAINT `prj001_generalinfo_owner_id_3383442a_fk_myusers_myuser_id` FOREIGN KEY (`owner_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prj001_generalinfo`
--

LOCK TABLES `prj001_generalinfo` WRITE;
/*!40000 ALTER TABLE `prj001_generalinfo` DISABLE KEYS */;
INSERT INTO `prj001_generalinfo` VALUES (35,'2018-11-30','243243241','汉典','王丽丽','主任医师  ','李芳芳','13367845788',33,177,56.2,'A','汉族',' 技术人员  ',0,1,0,0,0,1,0,1,'                    北京','门诊',' 本科  ','已婚同居',0,0,0,0,1,0,0,1,1,'True',14);
/*!40000 ALTER TABLE `prj001_generalinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prj001_investfileupload`
--

DROP TABLE IF EXISTS `prj001_investfileupload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prj001_investfileupload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `ivfile` varchar(100) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `prj001_investfileupload_owner_id_9049d149_fk_myusers_myuser_id` (`owner_id`),
  CONSTRAINT `prj001_investfileupload_owner_id_9049d149_fk_myusers_myuser_id` FOREIGN KEY (`owner_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prj001_investfileupload`
--

LOCK TABLES `prj001_investfileupload` WRITE;
/*!40000 ALTER TABLE `prj001_investfileupload` DISABLE KEYS */;
INSERT INTO `prj001_investfileupload` VALUES (95,'test','avatars/2018-11-30/13-55/07排卵障碍性异常子宫出血问卷_20181126.xlsx',14);
/*!40000 ALTER TABLE `prj001_investfileupload` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prj001_menstruation`
--

DROP TABLE IF EXISTS `prj001_menstruation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prj001_menstruation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_time` int(11) NOT NULL,
  `cyclicity` tinyint(1) NOT NULL,
  `normal` int(11) DEFAULT NULL,
  `abnormal` varchar(30) DEFAULT NULL,
  `cyclicity_sum` varchar(100) NOT NULL,
  `blood_cond` varchar(100) NOT NULL,
  `blood_color` varchar(10) NOT NULL,
  `blood_quality` varchar(10) NOT NULL,
  `blood_block` varchar(30) NOT NULL,
  `blood_character` varchar(20) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  KEY `prj001_menstruation_owner_id_203d30ff_fk_myusers_myuser_id` (`owner_id`),
  CONSTRAINT `prj001_menstruation_owner_id_203d30ff_fk_myusers_myuser_id` FOREIGN KEY (`owner_id`) REFERENCES `myusers_myuser` (`id`),
  CONSTRAINT `prj001_menstruation_person_id_45d3e179_fk_prj001_generalinfo_id` FOREIGN KEY (`person_id`) REFERENCES `prj001_generalinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prj001_menstruation`
--

LOCK TABLES `prj001_menstruation` WRITE;
/*!40000 ALTER TABLE `prj001_menstruation` DISABLE KEYS */;
INSERT INTO `prj001_menstruation` VALUES (24,12,0,NULL,'或提前7天以上',' 3-7天    ',' 出血量中等，每次约需5-20张卫生巾  ',' 鲜红  ','粘稠','常夹少量小血块','势急暴下',14,35);
/*!40000 ALTER TABLE `prj001_menstruation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prj001_other`
--

DROP TABLE IF EXISTS `prj001_other`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prj001_other` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hobbies_wu` tinyint(1) NOT NULL,
  `hobbies_xiyan` tinyint(1) NOT NULL,
  `hobbies_yinjiu` tinyint(1) NOT NULL,
  `hobbies_qita` varchar(50) NOT NULL,
  `body_cond` varchar(20) NOT NULL,
  `career_labor` varchar(100) NOT NULL,
  `poor_blood` varchar(20) NOT NULL,
  `phycial_exercise` varchar(50) NOT NULL,
  `reducefat_ever` tinyint(1) NOT NULL,
  `reducefat_yundong` tinyint(1) NOT NULL,
  `reducefat_jieshi` tinyint(1) NOT NULL,
  `reducefat_yaowu` tinyint(1) NOT NULL,
  `reducefat_qita` varchar(50) NOT NULL,
  `reducefat_persist` int(11) DEFAULT NULL,
  `mens_yundong` varchar(10) NOT NULL,
  `mens_ganmao` varchar(10) NOT NULL,
  `mens_tongfang` varchar(10) NOT NULL,
  `mens_zhaoliang` varchar(10) NOT NULL,
  `leucorrhea_liangshao` tinyint(1) NOT NULL,
  `leucorrhea_liangke` tinyint(1) NOT NULL,
  `leucorrhea_liangduo` tinyint(1) NOT NULL,
  `leucorrhea_sehuang` tinyint(1) NOT NULL,
  `leucorrhea_sebai` tinyint(1) NOT NULL,
  `leucorrhea_selv` tinyint(1) NOT NULL,
  `leucorrhea_zhiqingxi` tinyint(1) NOT NULL,
  `leucorrhea_zhinianchou` tinyint(1) NOT NULL,
  `pasthistory_wu` tinyint(1) NOT NULL,
  `pasthistory_yuejingbutiao` tinyint(1) NOT NULL,
  `pasthistory_yindaoyan` tinyint(1) NOT NULL,
  `pasthistory_zigongneimoyan` tinyint(1) NOT NULL,
  `pasthistory_zigongneimoyiwei` tinyint(1) NOT NULL,
  `pasthistory_zigongxianjizheng` tinyint(1) NOT NULL,
  `pasthistory_penqiangyan` tinyint(1) NOT NULL,
  `pasthistory_zigongjiliu` tinyint(1) NOT NULL,
  `pasthistory_luancaonangzhong` tinyint(1) NOT NULL,
  `pasthistory_ruxianzengsheng` tinyint(1) NOT NULL,
  `pasthistory_jiazhuangxian` tinyint(1) NOT NULL,
  `pasthistory_shengzhiyichang` tinyint(1) NOT NULL,
  `pasthistory_naochuitiliu` tinyint(1) NOT NULL,
  `pasthistory_feipang` tinyint(1) NOT NULL,
  `pasthistory_ganyan` tinyint(1) NOT NULL,
  `pasthistory_jiehe` tinyint(1) NOT NULL,
  `pasthistory_qita` varchar(50) NOT NULL,
  `pastmens_zhouqiwenluan` tinyint(1) NOT NULL,
  `pastmens_liangduo` tinyint(1) NOT NULL,
  `pastmens_zhouqisuoduan` tinyint(1) NOT NULL,
  `pastmens_yanhou` tinyint(1) NOT NULL,
  `pastmens_yanchang` tinyint(1) NOT NULL,
  `pastmens_tingbi` tinyint(1) NOT NULL,
  `pastmens_chuxie` tinyint(1) NOT NULL,
  `womb_blood` varchar(10) NOT NULL,
  `ovulation` varchar(10) NOT NULL,
  `pastfamily_wu` tinyint(1) NOT NULL,
  `pastfamily_gaoxueya` tinyint(1) NOT NULL,
  `pastfamily_tangniaobing` tinyint(1) NOT NULL,
  `pastfamily_xinzangbing` tinyint(1) NOT NULL,
  `pastfamily_duonangluanchao` tinyint(1) NOT NULL,
  `pastfamily_buxiang` tinyint(1) NOT NULL,
  `pastfamily_qita` varchar(50) NOT NULL,
  `pastpreg_yuncount` varchar(20) NOT NULL,
  `pastpreg_pougong` varchar(10) DEFAULT NULL,
  `pastpreg_shunchan` varchar(10) DEFAULT NULL,
  `pastpreg_yaoliu` varchar(10) DEFAULT NULL,
  `pastpreg_renliu` varchar(10) DEFAULT NULL,
  `pastpreg_ziranliu` varchar(10) DEFAULT NULL,
  `pastpreg_shenghuarenshen` varchar(10) DEFAULT NULL,
  `pastpreg_yiweirenshen` varchar(10) DEFAULT NULL,
  `pastpreg_taitingyu` varchar(10) DEFAULT NULL,
  `pastpreg_qinggongshu` varchar(10) DEFAULT NULL,
  `prevent_jieza` tinyint(1) NOT NULL,
  `prevent_jieyuqi` tinyint(1) NOT NULL,
  `prevent_biyuntao` tinyint(1) NOT NULL,
  `prevent_biyunyao` tinyint(1) NOT NULL,
  `prevent_biyunyao_time` decimal(3,1) DEFAULT NULL,
  `prevent_mafulong` tinyint(1) NOT NULL,
  `prevent_daying` tinyint(1) NOT NULL,
  `prevent_yousiming` tinyint(1) NOT NULL,
  `prevent_zuoque` tinyint(1) NOT NULL,
  `prevent_fufang` tinyint(1) NOT NULL,
  `prevent_qita` varchar(100) NOT NULL,
  `accessory_hgb_value` varchar(20) DEFAULT NULL,
  `accessory_quanxuexibaojishu` varchar(500) DEFAULT NULL,
  `accessory_chuxuexingjibing` varchar(100) DEFAULT NULL,
  `accessory_ningxue` varchar(100) DEFAULT NULL,
  `accessory_jiazhuangxian` varchar(100) DEFAULT NULL,
  `accessory_niaorenshen` varchar(100) DEFAULT NULL,
  `accessory_penqiangchaosheng` varchar(100) DEFAULT NULL,
  `accessory_jichutiwen` varchar(100) DEFAULT NULL,
  `accessory_jisushuiping` varchar(100) DEFAULT NULL,
  `accessory_guagong` varchar(100) DEFAULT NULL,
  `accessory_qita` varchar(100) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  `born_pougongchan` tinyint(1) NOT NULL,
  `born_yindaofenmian` tinyint(1) NOT NULL,
  `born_zaochan` tinyint(1) NOT NULL,
  `born_zuyuechan` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  KEY `prj001_other_owner_id_76f86c3a_fk_myusers_myuser_id` (`owner_id`),
  CONSTRAINT `prj001_other_owner_id_76f86c3a_fk_myusers_myuser_id` FOREIGN KEY (`owner_id`) REFERENCES `myusers_myuser` (`id`),
  CONSTRAINT `prj001_other_person_id_14f90708_fk_prj001_generalinfo_id` FOREIGN KEY (`person_id`) REFERENCES `prj001_generalinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prj001_other`
--

LOCK TABLES `prj001_other` WRITE;
/*!40000 ALTER TABLE `prj001_other` DISABLE KEYS */;
INSERT INTO `prj001_other` VALUES (8,0,0,0,'False','无','无','无','无',1,1,1,1,'无',0,'无','无','无','无',0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,'无',1,0,0,1,0,0,0,'无','无',0,0,0,0,1,0,'无','无','无','无','无','无','无','无','无','无','无',0,0,0,0,NULL,0,0,0,0,0,'无',' 91-110  ','红细胞计数(RBC) 5.0*10^12/L','无','无','无','无','无','无','无','无','无',14,35,1,1,1,0);
/*!40000 ALTER TABLE `prj001_other` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prj001_symptom`
--

DROP TABLE IF EXISTS `prj001_symptom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prj001_symptom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spirit_jinglichongpei` tinyint(1) NOT NULL,
  `spirit_jianwang` tinyint(1) NOT NULL,
  `spirit_jingshenbujizhong` tinyint(1) NOT NULL,
  `spirit_shenpifali` tinyint(1) NOT NULL,
  `spirit_yalida` tinyint(1) NOT NULL,
  `spirit_jiaodabiangu` tinyint(1) NOT NULL,
  `spirit_beishangyuku` tinyint(1) NOT NULL,
  `mood_zhengchang` tinyint(1) NOT NULL,
  `mood_leguankailang` tinyint(1) NOT NULL,
  `mood_silvguodu` tinyint(1) NOT NULL,
  `mood_xinuwuchang` tinyint(1) NOT NULL,
  `mood_fanzaoyinu` tinyint(1) NOT NULL,
  `mood_jiaolv` tinyint(1) NOT NULL,
  `mood_beishangyuku` tinyint(1) NOT NULL,
  `mood_yiyu` tinyint(1) NOT NULL,
  `mood_duosiduolv` tinyint(1) NOT NULL,
  `mood_qita` varchar(50) NOT NULL,
  `chillfever_zhengchang` tinyint(1) NOT NULL,
  `chillfever_weihan` tinyint(1) NOT NULL,
  `chillfever_wuxinfanre` tinyint(1) NOT NULL,
  `chillfever_wuhouchaore` tinyint(1) NOT NULL,
  `chillfever_direbutui` tinyint(1) NOT NULL,
  `sweat_zhengchang` tinyint(1) NOT NULL,
  `sweat_duohan` tinyint(1) NOT NULL,
  `sweat_mingxian` tinyint(1) NOT NULL,
  `sweat_zihan` tinyint(1) NOT NULL,
  `sweat_daohan` tinyint(1) NOT NULL,
  `sweat_hongre` tinyint(1) NOT NULL,
  `sweat_chaore` tinyint(1) NOT NULL,
  `sound_zhengchang` tinyint(1) NOT NULL,
  `sound_qiduan` tinyint(1) NOT NULL,
  `sound_xitanxi` tinyint(1) NOT NULL,
  `sound_shaoqilanyan` tinyint(1) NOT NULL,
  `face_zhengchang` tinyint(1) NOT NULL,
  `face_danbaiwuhua` tinyint(1) NOT NULL,
  `face_cangbai` tinyint(1) NOT NULL,
  `face_qingbai` tinyint(1) NOT NULL,
  `face_weihuang` tinyint(1) NOT NULL,
  `face_huangzhong` tinyint(1) NOT NULL,
  `face_chaohong` tinyint(1) NOT NULL,
  `face_huian` tinyint(1) NOT NULL,
  `face_baierfuzhong` tinyint(1) NOT NULL,
  `face_baierandan` tinyint(1) NOT NULL,
  `face_mianmulihei` tinyint(1) NOT NULL,
  `face_shaohua` tinyint(1) NOT NULL,
  `face_wuhua` tinyint(1) NOT NULL,
  `heart_zhengcheng` tinyint(1) NOT NULL,
  `heart_xinfan` tinyint(1) NOT NULL,
  `heart_xinji` tinyint(1) NOT NULL,
  `breast_zhengchang` tinyint(1) NOT NULL,
  `breast_biezhang` tinyint(1) NOT NULL,
  `breast_citong` tinyint(1) NOT NULL,
  `breast_zhangtong` tinyint(1) NOT NULL,
  `breast_chutong` tinyint(1) NOT NULL,
  `chest_zhengchang` tinyint(1) NOT NULL,
  `chest_zhangmen` tinyint(1) NOT NULL,
  `chest_yintong` tinyint(1) NOT NULL,
  `chest_citong` tinyint(1) NOT NULL,
  `waist_zhengchang` tinyint(1) NOT NULL,
  `waist_suantong` tinyint(1) NOT NULL,
  `waist_suanruan` tinyint(1) NOT NULL,
  `waist_suanleng` tinyint(1) NOT NULL,
  `waist_lengtong` tinyint(1) NOT NULL,
  `waist_yaotongrushe` tinyint(1) NOT NULL,
  `stomach_zhengchang` tinyint(1) NOT NULL,
  `stomach_zhangtongjuan` tinyint(1) NOT NULL,
  `stomach_xiaofuzhuizhang` tinyint(1) NOT NULL,
  `stomach_xiaofubiezhang` tinyint(1) NOT NULL,
  `stomach_xiaofulengtong` tinyint(1) NOT NULL,
  `stomach_xiaofuzhuotong` tinyint(1) NOT NULL,
  `stomach_yintongxian` tinyint(1) NOT NULL,
  `stomach_dewentongjian` tinyint(1) NOT NULL,
  `stomach_tongruzhenci` tinyint(1) NOT NULL,
  `stomach_kongzhui` tinyint(1) NOT NULL,
  `head_zhengchang` tinyint(1) NOT NULL,
  `head_touyun` tinyint(1) NOT NULL,
  `head_toutong` tinyint(1) NOT NULL,
  `head_touchenzhong` tinyint(1) NOT NULL,
  `eyes_zhengchang` tinyint(1) NOT NULL,
  `eyes_muxuan` tinyint(1) NOT NULL,
  `eyes_muse` tinyint(1) NOT NULL,
  `eyes_yanhua` tinyint(1) NOT NULL,
  `eyes_mutong` tinyint(1) NOT NULL,
  `eyes_muyang` tinyint(1) NOT NULL,
  `eyes_chenqifz` tinyint(1) NOT NULL,
  `ear_erming` tinyint(1) NOT NULL,
  `ear_erlong` tinyint(1) NOT NULL,
  `ear_tinglibq` tinyint(1) NOT NULL,
  `throat_zhengchang` tinyint(1) NOT NULL,
  `throat_yangan` tinyint(1) NOT NULL,
  `throat_yantong` tinyint(1) NOT NULL,
  `throat_yanyang` tinyint(1) NOT NULL,
  `throat_yiwugan` tinyint(1) NOT NULL,
  `breath_wuyiwei` tinyint(1) NOT NULL,
  `breath_kouku` tinyint(1) NOT NULL,
  `breath_kougan` tinyint(1) NOT NULL,
  `breath_koudan` tinyint(1) NOT NULL,
  `breath_kouxian` tinyint(1) NOT NULL,
  `breath_koutian` tinyint(1) NOT NULL,
  `breath_kounian` tinyint(1) NOT NULL,
  `breath_danyuss` tinyint(1) NOT NULL,
  `diet_nadaishishao` tinyint(1) NOT NULL,
  `diet_shiyuws` tinyint(1) NOT NULL,
  `diet_yanshi` tinyint(1) NOT NULL,
  `diet_xireyin` tinyint(1) NOT NULL,
  `diet_xilengyin` tinyint(1) NOT NULL,
  `diet_shiyujiantui` tinyint(1) NOT NULL,
  `diet_shihoufuzhang` tinyint(1) NOT NULL,
  `diet_shixinla` tinyint(1) NOT NULL,
  `diet_shishengleng` tinyint(1) NOT NULL,
  `diet_kebuduoyin` tinyint(1) NOT NULL,
  `sleep_zhengchang` tinyint(1) NOT NULL,
  `sleep_yiban` tinyint(1) NOT NULL,
  `sleep_duomengyixing` tinyint(1) NOT NULL,
  `sleep_nanyirumian` tinyint(1) NOT NULL,
  `sleep_cheyebumian` tinyint(1) NOT NULL,
  `sleep_duomeng` tinyint(1) NOT NULL,
  `sleep_shishui` tinyint(1) NOT NULL,
  `stool_sehuang` tinyint(1) NOT NULL,
  `stool_bianmi` tinyint(1) NOT NULL,
  `stool_zhixi` tinyint(1) NOT NULL,
  `stool_sgsx` tinyint(1) NOT NULL,
  `stool_xiexie` tinyint(1) NOT NULL,
  `stool_tlzqxiexie` tinyint(1) NOT NULL,
  `stool_zhinian` tinyint(1) NOT NULL,
  `stool_weixiaohua` tinyint(1) NOT NULL,
  `urine_zhengchang` tinyint(1) NOT NULL,
  `urine_duanchi` tinyint(1) NOT NULL,
  `urine_duanhuang` tinyint(1) NOT NULL,
  `urine_qingchang` tinyint(1) NOT NULL,
  `urine_yeniaopin` tinyint(1) NOT NULL,
  `urine_xbpinshu` tinyint(1) NOT NULL,
  `urine_niaoji` tinyint(1) NOT NULL,
  `urine_niaotong` tinyint(1) NOT NULL,
  `urine_shaoniao` tinyint(1) NOT NULL,
  `urine_yulibujin` tinyint(1) NOT NULL,
  `limb_zhengchang` tinyint(1) NOT NULL,
  `limb_wuli` tinyint(1) NOT NULL,
  `limb_mamu` tinyint(1) NOT NULL,
  `limb_kunzhong` tinyint(1) NOT NULL,
  `limb_zhileng` tinyint(1) NOT NULL,
  `limb_bingliang` tinyint(1) NOT NULL,
  `limb_szxinre` tinyint(1) NOT NULL,
  `limb_fuzhong` tinyint(1) NOT NULL,
  `other_wu` tinyint(1) NOT NULL,
  `other_czjdanbai` tinyint(1) NOT NULL,
  `other_xyjiantui` tinyint(1) NOT NULL,
  `texture_danhong` tinyint(1) NOT NULL,
  `texture_danbai` tinyint(1) NOT NULL,
  `texture_pianhong` tinyint(1) NOT NULL,
  `texture_danan` tinyint(1) NOT NULL,
  `texture_zian` tinyint(1) NOT NULL,
  `texture_yudian` tinyint(1) NOT NULL,
  `coating_bai` tinyint(1) NOT NULL,
  `coating_huang` tinyint(1) NOT NULL,
  `coating_ni` tinyint(1) NOT NULL,
  `coating_bo` tinyint(1) NOT NULL,
  `coating_hou` tinyint(1) NOT NULL,
  `coating_run` tinyint(1) NOT NULL,
  `coating_hua` tinyint(1) NOT NULL,
  `coating_hhouni` tinyint(1) NOT NULL,
  `coating_bairun` tinyint(1) NOT NULL,
  `coating_huangcao` tinyint(1) NOT NULL,
  `coating_wutai` tinyint(1) NOT NULL,
  `coating_shaotai` tinyint(1) NOT NULL,
  `coating_huabo` tinyint(1) NOT NULL,
  `tongue_shoubo` tinyint(1) NOT NULL,
  `tongue_pangda` tinyint(1) NOT NULL,
  `tongue_bianjianhong` tinyint(1) NOT NULL,
  `tongue_youchihen` tinyint(1) NOT NULL,
  `tongue_zhongyouliewen` tinyint(1) NOT NULL,
  `pulse_shi` tinyint(1) NOT NULL,
  `pulse_fu` tinyint(1) NOT NULL,
  `pulse_chen` tinyint(1) NOT NULL,
  `pulse_chi` tinyint(1) NOT NULL,
  `pulse_huan` tinyint(1) NOT NULL,
  `pulse_xi` tinyint(1) NOT NULL,
  `pulse_ruo` tinyint(1) NOT NULL,
  `pulse_shu` tinyint(1) NOT NULL,
  `pulse_hua` tinyint(1) NOT NULL,
  `pulse_se` tinyint(1) NOT NULL,
  `pulse_xian` tinyint(1) NOT NULL,
  `pulse_jin` tinyint(1) NOT NULL,
  `pulse_kou` tinyint(1) NOT NULL,
  `pulse_ru` tinyint(1) NOT NULL,
  `pulse_hong` tinyint(1) NOT NULL,
  `pulse_youli` tinyint(1) NOT NULL,
  `pulse_wuli` tinyint(1) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  KEY `prj001_symptom_owner_id_a7888863_fk_myusers_myuser_id` (`owner_id`),
  CONSTRAINT `prj001_symptom_owner_id_a7888863_fk_myusers_myuser_id` FOREIGN KEY (`owner_id`) REFERENCES `myusers_myuser` (`id`),
  CONSTRAINT `prj001_symptom_person_id_1fb707d1_fk_prj001_generalinfo_id` FOREIGN KEY (`person_id`) REFERENCES `prj001_generalinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prj001_symptom`
--

LOCK TABLES `prj001_symptom` WRITE;
/*!40000 ALTER TABLE `prj001_symptom` DISABLE KEYS */;
INSERT INTO `prj001_symptom` VALUES (18,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,'False',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,14,35);
/*!40000 ALTER TABLE `prj001_symptom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_clinicalprojects`
--

DROP TABLE IF EXISTS `projects_clinicalprojects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects_clinicalprojects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `prj_code` varchar(100) NOT NULL,
  `status` varchar(10) NOT NULL,
  `starttime` date NOT NULL,
  `endtime` date NOT NULL,
  `linkurl` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_clinicalprojects`
--

LOCK TABLES `projects_clinicalprojects` WRITE;
/*!40000 ALTER TABLE `projects_clinicalprojects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_clinicalprojects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_clinicalprojects_relusers`
--

DROP TABLE IF EXISTS `projects_clinicalprojects_relusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects_clinicalprojects_relusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clinicalprojects_id` int(11) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `projects_clinicalproject_clinicalprojects_id_myus_f8537c8c_uniq` (`clinicalprojects_id`,`myuser_id`),
  KEY `projects_clinicalpro_myuser_id_ac3111ea_fk_myusers_m` (`myuser_id`),
  CONSTRAINT `projects_clinicalpro_clinicalprojects_id_b42b4353_fk_projects_` FOREIGN KEY (`clinicalprojects_id`) REFERENCES `projects_clinicalprojects` (`id`),
  CONSTRAINT `projects_clinicalpro_myuser_id_ac3111ea_fk_myusers_m` FOREIGN KEY (`myuser_id`) REFERENCES `myusers_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_clinicalprojects_relusers`
--

LOCK TABLES `projects_clinicalprojects_relusers` WRITE;
/*!40000 ALTER TABLE `projects_clinicalprojects_relusers` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_clinicalprojects_relusers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-30 14:10:19
