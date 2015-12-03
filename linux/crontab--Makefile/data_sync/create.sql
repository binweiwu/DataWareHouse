DROP TABLE IF EXISTS `uc_area_group`;
CREATE TABLE `uc_area_group` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `createDate` datetime DEFAULT NULL,
  `updateDate` datetime DEFAULT NULL,
  `version` bigint(20) DEFAULT NULL,
  `areaId` bigint(20) DEFAULT NULL,
  `areaName` varchar(255) DEFAULT NULL,
  `groupName` varchar(255) DEFAULT NULL,
  `groupId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `uc_apply`;
CREATE TABLE `uc_apply` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `createDate` datetime DEFAULT NULL,
  `updateDate` datetime DEFAULT NULL,
  `version` bigint(20) DEFAULT NULL,
  `applyTarget` varchar(255) DEFAULT NULL,
  `area2Id` bigint(20) DEFAULT NULL,
  `area2Name` varchar(255) DEFAULT NULL,
  `idCard` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `realName` varchar(255) DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `schoolId` bigint(20) DEFAULT NULL,
  `schoolName` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `universityId` bigint(20) DEFAULT NULL,
  `universityName` varchar(255) DEFAULT NULL,
  `userId` bigint(20) DEFAULT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `referee` varchar(20) DEFAULT NULL,
  `refuseReason` varchar(255) DEFAULT NULL,
  `createUserId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=472 DEFAULT CHARSET=utf8;


