-- MariaDB dump 10.19  Distrib 10.4.27-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: projeto_final
-- ------------------------------------------------------
-- Server version	10.4.27-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Encomendas`
--

DROP TABLE IF EXISTS `Encomendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Encomendas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`),
  CONSTRAINT `Encomendas_ibfk_1` FOREIGN KEY (`user`) REFERENCES `Utilizadores` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Encomendas`
--

LOCK TABLES `Encomendas` WRITE;
/*!40000 ALTER TABLE `Encomendas` DISABLE KEYS */;
INSERT INTO `Encomendas` VALUES (1,'user6');
/*!40000 ALTER TABLE `Encomendas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Produtos`
--

DROP TABLE IF EXISTS `Produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Produtos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` float(6,2) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Produtos`
--

LOCK TABLES `Produtos` WRITE;
/*!40000 ALTER TABLE `Produtos` DISABLE KEYS */;
INSERT INTO `Produtos` VALUES (1,'blue dino shirt',11.99,50,'pictures/img_002.jpeg'),(2,'yellow dino shirt',11.99,32,'pictures/img_003.jpeg'),(3,'banana palms shirt',14.99,30,'pictures/img_004.jpeg'),(4,'white dino shirt',12.50,18,'pictures/img_005.jpeg'),(5,'green dino sweater',16.99,12,'pictures/img_006.jpeg'),(6,'white orange shirt',15.50,16,'pictures/img_007.jpeg'),(7,'blue cake dress',20.00,8,'pictures/img_008.jpeg'),(9,'white fruit dress',22.00,12,'pictures/img_009.jpeg'),(10,'white blue striped',9.99,22,'pictures/img_010.jpeg'),(11,'blue green plane set',15.99,14,'pictures/img_011.jpeg'),(12,'blue green dress',14.99,1,'pictures/img_012.jpeg'),(13,'blue elephant set',12.99,4,'pictures/img_013.jpeg'),(14,'black shirt',7.99,0,'pictures/img_014.jpeg'),(15,'pink elephant set',12.99,7,'pictures/img_015.jpeg'),(16,'pink dress',10.99,7,'pictures/img_016.jpeg'),(17,'blue dress set',14.00,10,'pictures/img_017.jpeg'),(18,'blue overalls',11.99,19,'pictures/img_018.jpeg'),(19,'dino shirt shorts set',12.99,8,'pictures/img_019.jpeg'),(20,'dino shirt shorts set 2',12.99,8,'pictures/img_020.jpeg'),(21,'blue shirt shorts set',10.99,21,'pictures/img_021.jpeg'),(22,'white blue shirt shorts set',13.99,12,'pictures/img_022.jpeg');
/*!40000 ALTER TABLE `Produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Utilizadores`
--

DROP TABLE IF EXISTS `Utilizadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Utilizadores` (
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `birthDate` date NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Utilizadores`
--

LOCK TABLES `Utilizadores` WRITE;
/*!40000 ALTER TABLE `Utilizadores` DISABLE KEYS */;
INSERT INTO `Utilizadores` VALUES ('admin','$2y$10$pl3v6DSUt1SqR9pjw64HSukckNStX0fLspY7QES3TH2nwaOsa4CLe','John Doe','New Street, n8, New County','1989-06-13'),('user1','$2y$10$4mSk9ccxXN6UX2O6aoklNO4c8fxusstHxvcrswFIs5qgMqHZZQR.a','user1','Random Street, n9, Random Place','2000-02-01'),('user2','$2y$10$BpKbr5cVnmSY6UEj6XCiVefDUb107uZHvkG6vhtCy/KQ6ZS6QuY16','user2','Random Street, n9, Random Place','1967-10-29'),('user3','$2y$10$NYR0IoD6X7Wq6luF8LScguN.oksRQhGYBw95sdfdPAdhVbUYaww6O','user3','Random Street, n21, Random Place','1964-01-22'),('user4','$2y$10$Td4ngWtIiT3QUV46oI8VxObkkBXIjTfsqLQYLC3gM0DGAx.PwLzH6','user4','Random Street, n21, Random Place','1990-02-01'),('user5','$2y$10$CBU2tjF3gEqb6lZIZ5h0auTXpN/LgBgAbsVKygK6W/yUPQtzFvU7S','user5','Random Place','1995-07-08'),('user6','$2y$10$1SC2AbWLLAmN2FTfT3Jad.w1Ow9qW1geILCQFobF.hgWzHhMxGy4q','user6','Random Street','1995-10-24');
/*!40000 ALTER TABLE `Utilizadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encomenda_info`
--

DROP TABLE IF EXISTS `encomenda_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encomenda_info` (
  `encomenda` int(11) NOT NULL,
  `product` int(11) NOT NULL,
  `quantity` smallint(6) NOT NULL,
  PRIMARY KEY (`encomenda`,`product`),
  KEY `product` (`product`),
  CONSTRAINT `encomenda_info_ibfk_2` FOREIGN KEY (`product`) REFERENCES `Produtos` (`id`),
  CONSTRAINT `encomenda_info_ibfk_3` FOREIGN KEY (`encomenda`) REFERENCES `Encomendas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encomenda_info`
--

LOCK TABLES `encomenda_info` WRITE;
/*!40000 ALTER TABLE `encomenda_info` DISABLE KEYS */;
INSERT INTO `encomenda_info` VALUES (1,17,2),(1,22,1);
/*!40000 ALTER TABLE `encomenda_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-07 23:17:52
