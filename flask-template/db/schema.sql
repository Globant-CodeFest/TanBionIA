-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	5.7.31
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO,POSTGRESQL' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: "proyecto"
--

--
-- Table structure for table "categories"
--

DROP TABLE IF EXISTS "categories" CASCADE;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE "categories" (
  "id" SERIAL primary key,
  "name" varchar(30) DEFAULT NULL
);

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "categories"
--
BEGIN WORK;
LOCK TABLE "categories" IN ACCESS EXCLUSIVE MODE;
/*!40000 ALTER TABLE "categories" DISABLE KEYS */;
INSERT INTO "categories" VALUES (1,'Bug'),(2,'Question');
/*!40000 ALTER TABLE "categories" ENABLE KEYS */;
COMMIT WORK;

SELECT setval('categories_id_seq', 2, true);

--
-- Table structure for table "statuses"
--

DROP TABLE IF EXISTS "statuses" CASCADE;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE "statuses" (
  "id" SERIAL primary key,
  "name" varchar(30) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "statuses"
--


BEGIN WORK;
LOCK TABLE "statuses" IN access EXCLUSIVE MODE;
/*!40000 ALTER TABLE "statuses" DISABLE KEYS */;
INSERT INTO "statuses" VALUES (1,'New'),(2,'Todo'),(3,'In progress');
/*!40000 ALTER TABLE "statuses" ENABLE KEYS */;
COMMIT WORK;

SELECT setval('statuses_id_seq', 3, true);

--
-- Table structure for table "issues"
--

DROP TABLE IF EXISTS "issues" CASCADE;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE "issues" (
  "id" SERIAL primary key,
  "email" varchar(30) DEFAULT NULL,
  "description" text,
  "category_id" int NOT NULL,
  "status_id" int NOT NULL,
  CONSTRAINT "issues_ibfk_1" FOREIGN KEY ("category_id") REFERENCES "categories" ("id"),
  CONSTRAINT "issues_ibfk_2" FOREIGN KEY ("status_id") REFERENCES "statuses" ("id")
);
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "issues"
--

BEGIN WORK;
LOCK TABLE "issues" IN access EXCLUSIVE MODE;
/*!40000 ALTER TABLE "issues" DISABLE KEYS */;
INSERT INTO "issues" VALUES (1,'fede@mail.com','No puedo iniciar sesi�n correctamente',1,1),(2,'jose@mail.com','El sistema de dice que hay un error',1,2),(3,'maria@mail.com','No tengo acceso al sistema',1,1);
/*!40000 ALTER TABLE "issues" ENABLE KEYS */;
COMMIT WORK;

SELECT setval('issues_id_seq', 3, true);


--
-- Table structure for table "users"
--

DROP TABLE IF EXISTS "users" CASCADE;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE "users" (
  "id" SERIAL primary key,
  "email" varchar(30) NOT NULL,
  "password" varchar(30) NOT NULL,
  "first_name" varchar(30) NOT NULL,
  "last_name" varchar(30) NOT NULL,
  UNIQUE("email", "password", "first_name", "last_name")
);
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "users"
--

BEGIN WORK;
LOCK TABLE "users" IN access EXCLUSIVE MODE;
/*!40000 ALTER TABLE "statuses" DISABLE KEYS */;
INSERT INTO "users" VALUES (1,'admin','123123','Cosme','Fulanito');
/*!40000 ALTER TABLE "statuses" ENABLE KEYS */;
COMMIT WORK;

SELECT setval('users_id_seq', 1, true);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-12 20:22:37
