/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50549
Source Host           : localhost:3306
Source Database       : qshop

Target Server Type    : MYSQL
Target Server Version : 50549
File Encoding         : 65001

Date: 2019-04-17 19:35:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add manager message', '7', 'add_managermessage');
INSERT INTO `auth_permission` VALUES ('20', 'Can change manager message', '7', 'change_managermessage');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete manager message', '7', 'delete_managermessage');
INSERT INTO `auth_permission` VALUES ('22', 'Can add power', '8', 'add_power');
INSERT INTO `auth_permission` VALUES ('23', 'Can change power', '8', 'change_power');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete power', '8', 'delete_power');
INSERT INTO `auth_permission` VALUES ('25', 'Can add power_roles', '9', 'add_power_roles');
INSERT INTO `auth_permission` VALUES ('26', 'Can change power_roles', '9', 'change_power_roles');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete power_roles', '9', 'delete_power_roles');
INSERT INTO `auth_permission` VALUES ('28', 'Can add roles', '10', 'add_roles');
INSERT INTO `auth_permission` VALUES ('29', 'Can change roles', '10', 'change_roles');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete roles', '10', 'delete_roles');
INSERT INTO `auth_permission` VALUES ('31', 'Can add goods info', '11', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can change goods info', '11', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete goods info', '11', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('34', 'Can add goods type', '12', 'add_goodstype');
INSERT INTO `auth_permission` VALUES ('35', 'Can change goods type', '12', 'change_goodstype');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete goods type', '12', 'delete_goodstype');
INSERT INTO `auth_permission` VALUES ('37', 'Can add car', '13', 'add_car');
INSERT INTO `auth_permission` VALUES ('38', 'Can change car', '13', 'change_car');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete car', '13', 'delete_car');
INSERT INTO `auth_permission` VALUES ('40', 'Can add comment', '14', 'add_comment');
INSERT INTO `auth_permission` VALUES ('41', 'Can change comment', '14', 'change_comment');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete comment', '14', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('43', 'Can add order_info', '15', 'add_order_info');
INSERT INTO `auth_permission` VALUES ('44', 'Can change order_info', '15', 'change_order_info');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete order_info', '15', 'delete_order_info');
INSERT INTO `auth_permission` VALUES ('46', 'Can add orders', '16', 'add_orders');
INSERT INTO `auth_permission` VALUES ('47', 'Can change orders', '16', 'change_orders');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete orders', '16', 'delete_orders');
INSERT INTO `auth_permission` VALUES ('49', 'Can add user_address', '17', 'add_user_address');
INSERT INTO `auth_permission` VALUES ('50', 'Can change user_address', '17', 'change_user_address');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete user_address', '17', 'delete_user_address');
INSERT INTO `auth_permission` VALUES ('52', 'Can add users', '18', 'add_users');
INSERT INTO `auth_permission` VALUES ('53', 'Can change users', '18', 'change_users');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete users', '18', 'delete_users');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('11', 'goods', 'goodsinfo');
INSERT INTO `django_content_type` VALUES ('12', 'goods', 'goodstype');
INSERT INTO `django_content_type` VALUES ('7', 'manager', 'managermessage');
INSERT INTO `django_content_type` VALUES ('8', 'manager', 'power');
INSERT INTO `django_content_type` VALUES ('9', 'manager', 'power_roles');
INSERT INTO `django_content_type` VALUES ('10', 'manager', 'roles');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('13', 'user', 'car');
INSERT INTO `django_content_type` VALUES ('14', 'user', 'comment');
INSERT INTO `django_content_type` VALUES ('16', 'user', 'orders');
INSERT INTO `django_content_type` VALUES ('15', 'user', 'order_info');
INSERT INTO `django_content_type` VALUES ('18', 'user', 'users');
INSERT INTO `django_content_type` VALUES ('17', 'user', 'user_address');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-22 09:52:28');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-12-22 09:52:28');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-12-22 09:52:28');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-12-22 09:52:28');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-12-22 09:52:28');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-12-22 09:52:28');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('13', 'manager', '0001_initial', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('14', 'goods', '0001_initial', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2018-12-22 09:52:29');
INSERT INTO `django_migrations` VALUES ('16', 'user', '0001_initial', '2018-12-22 09:52:29');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1s3ipkvwouag1flypvu1r5izj653a5kz', 'ZTcwNjNjN2YxMWU1NGM0YTU4YWMwNDc0ZTgxNDU5MzRkNWUwMzlhNjp7InZlcmlmeV9jb2RlIjoiOWQzeDgifQ==', '2019-04-27 10:32:33');
INSERT INTO `django_session` VALUES ('ajt6nj89tollxdkc1f9asbqhdid4pk2f', 'NGY0ZGU0NWMzNDBiNjk1NjA4MTZjMmQ1NGNhZTc3MjQxODRjYjUwYzp7InZlcmlmeV9jb2RlIjoiMjI5aGkifQ==', '2019-03-04 03:13:53');
INSERT INTO `django_session` VALUES ('ayz9ejlbni46i9syeh7njotqqc9qtdnu', 'NzZkNDYyOTE4YjA2ZDkyZGQwZTNlYzI3NGJhNDJjZmIyYTEzOWUxMjp7InZlcmlmeV9jb2RlIjoid20zYWoifQ==', '2019-03-01 08:22:40');
INSERT INTO `django_session` VALUES ('pfyytfoan964fwdjnx1o1isr941ge0p4', 'NmJjZWExNzk4N2UwZDkzY2E4YzZlZTJkYzAwNTQ5ZTk3ZWM1OTBmNDp7InZlcmlmeV9jb2RlIjoiNXo2dmwiLCJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MywidXNlcl9wb3dlcl9saXN0IjpbXX0=', '2019-01-05 10:05:42');
INSERT INTO `django_session` VALUES ('u6dixkov9md3ov05h1o4yiyxutch5oxm', 'ODA3OGZkODdmYjhhMGIyNjllYmNkOWMwZGIyZTA3YmUxNTVmNjRjMjp7InVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjozLCJ1c2VyX3Bvd2VyX2xpc3QiOltdfQ==', '2019-01-16 11:00:11');
INSERT INTO `django_session` VALUES ('wxgbawgzot2s4jwvs4zw9eclp5kwscp6', 'YzEzNGQ4ZTI2OGRjZTkxOTFiNWFlNjY3ZDVjZGQxMDFjMWM3ZGExMjp7InZlcmlmeV9jb2RlIjoiNnlxMHQiLCJ1c2VybmFtZSI6ImxsIiwidXNlcl9pZCI6NSwidXNlcl9wb3dlcl9saXN0IjpbXX0=', '2019-01-07 02:12:01');
INSERT INTO `django_session` VALUES ('x59ttxxjtk8t1i2ieuqeu84efgwxwyrr', 'ZmZlOTI0MWFhZTQxNmY2N2I4Y2I1OGVlMjE0NTY5MzNjNmU3MjI4Mzp7InZlcmlmeV9jb2RlIjoiaG1jcGMiLCJ0ZW1wX3VpZCI6MSwiVV91c2VyaWQiOjEsIlVfdXNlcm5hbWUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjozLCJ1c2VyX3Bvd2VyX2xpc3QiOltdfQ==', '2019-04-27 11:52:52');
INSERT INTO `django_session` VALUES ('yukanxp55uo3mjywuq4vn4lb90gvlon3', 'ODA3OGZkODdmYjhhMGIyNjllYmNkOWMwZGIyZTA3YmUxNTVmNjRjMjp7InVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjozLCJ1c2VyX3Bvd2VyX2xpc3QiOltdfQ==', '2019-01-11 11:31:18');

-- ----------------------------
-- Table structure for goods_goodsinfo
-- ----------------------------
DROP TABLE IF EXISTS `goods_goodsinfo`;
CREATE TABLE `goods_goodsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_num` varchar(20) NOT NULL,
  `goods_name` varchar(200) NOT NULL,
  `goods_oprice` double NOT NULL,
  `goods_xprice` double NOT NULL,
  `goods_count` int(11) NOT NULL,
  `goods_method` varchar(100) NOT NULL,
  `goods_info` varchar(100) NOT NULL,
  `goods_pic` varchar(100) NOT NULL,
  `goods_address` varchar(50) NOT NULL,
  `goods_content` longtext NOT NULL,
  `manager_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodsinfo_manager_id_a23939c1_fk_manager_managermessage_id` (`manager_id`),
  KEY `goods_goodsinfo_type_id_357bffcb_fk_goods_goodstype_type_id` (`type_id`),
  CONSTRAINT `goods_goodsinfo_manager_id_a23939c1_fk_manager_managermessage_id` FOREIGN KEY (`manager_id`) REFERENCES `manager_managermessage` (`id`),
  CONSTRAINT `goods_goodsinfo_type_id_357bffcb_fk_goods_goodstype_type_id` FOREIGN KEY (`type_id`) REFERENCES `goods_goodstype` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goodsinfo
-- ----------------------------
INSERT INTO `goods_goodsinfo` VALUES ('1', '1', '红苹果', '10', '8', '1000', '常温', '这是一个红苹果', '/media/uploads/798081c8-05d1-11e9-9140-9cda3e9c037d.jpg', '北京', '<img src=\"/media/kindeditor/2018/12/6daa2c30-05d1-11e9-be9e-9cda3e9c037d.jpg\" alt=\"\" width=\"350\" height=\"327\" title=\"\" align=\"\" />', '3', '1');
INSERT INTO `goods_goodsinfo` VALUES ('2', '1', '红苹果', '10', '8', '1000', '常温', '这是一个红苹果', '/media/uploads/7ba54f34-05d1-11e9-9690-9cda3e9c037d.jpg', '北京', '<img src=\"/media/kindeditor/2018/12/6daa2c30-05d1-11e9-be9e-9cda3e9c037d.jpg\" alt=\"\" width=\"350\" height=\"327\" title=\"\" align=\"\" />', '3', '1');
INSERT INTO `goods_goodsinfo` VALUES ('3', '3', '青苹果', '99', '98', '99', '常温', '这是一个有点酸又有点甜的苹果。', '/media/uploads/a78bf0a8-0721-11e9-b3c2-9cda3e9c037d.jpg', '铜仁', '<img src=\"/media/kindeditor/2018/12/a0e77fda-0721-11e9-9a5a-9cda3e9c037d.jpg\" alt=\"\" width=\"350\" height=\"202\" title=\"\" align=\"\" />', '5', '1');

-- ----------------------------
-- Table structure for goods_goodstype
-- ----------------------------
DROP TABLE IF EXISTS `goods_goodstype`;
CREATE TABLE `goods_goodstype` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(30) NOT NULL,
  `type_sort` int(11) NOT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goodstype
-- ----------------------------
INSERT INTO `goods_goodstype` VALUES ('1', '水果', '1');

-- ----------------------------
-- Table structure for manager_managermessage
-- ----------------------------
DROP TABLE IF EXISTS `manager_managermessage`;
CREATE TABLE `manager_managermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `userpass` varchar(32) NOT NULL,
  `nicheng` varchar(30) DEFAULT NULL,
  `shop_name` varchar(50) DEFAULT NULL,
  `shop_logo` varchar(50) DEFAULT NULL,
  `shop_address` varchar(100) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_managermessage_role_id_98b3748e_fk_manager_roles_id` (`role_id`),
  CONSTRAINT `manager_managermessage_role_id_98b3748e_fk_manager_roles_id` FOREIGN KEY (`role_id`) REFERENCES `manager_roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_managermessage
-- ----------------------------
INSERT INTO `manager_managermessage` VALUES ('2', '刘欢', '000000', 'lh', '青苹果乐园', 'media/uploads/u5745514804206807503fm27_8x6igoD.jpg', '北京', '1');
INSERT INTO `manager_managermessage` VALUES ('3', 'admin', '000000', 'lanlan', '红苹果乐园', 'media/uploads/u15244725582981168001fm26gp0.jpg', '北京', '1');
INSERT INTO `manager_managermessage` VALUES ('4', 'adminer', '000000', 'lll', '草莓乐园', 'media/uploads/u19672836042782645775fm200gp0.jpg', '铜仁', '1');
INSERT INTO `manager_managermessage` VALUES ('5', 'll', '000000', '罗昌兰', '水果超市', 'media/uploads/u3892392241604156840fm26gp0.jpg', '铜仁', '1');

-- ----------------------------
-- Table structure for manager_power
-- ----------------------------
DROP TABLE IF EXISTS `manager_power`;
CREATE TABLE `manager_power` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `url` varchar(50) NOT NULL,
  `add_time` datetime NOT NULL,
  `add_user` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_power
-- ----------------------------

-- ----------------------------
-- Table structure for manager_power_roles
-- ----------------------------
DROP TABLE IF EXISTS `manager_power_roles`;
CREATE TABLE `manager_power_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `power_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_power_roles_power_id_c33e409a_fk_manager_power_id` (`power_id`),
  KEY `manager_power_roles_role_id_ba8d8726_fk_manager_roles_id` (`role_id`),
  CONSTRAINT `manager_power_roles_power_id_c33e409a_fk_manager_power_id` FOREIGN KEY (`power_id`) REFERENCES `manager_power` (`id`),
  CONSTRAINT `manager_power_roles_role_id_ba8d8726_fk_manager_roles_id` FOREIGN KEY (`role_id`) REFERENCES `manager_roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_power_roles
-- ----------------------------

-- ----------------------------
-- Table structure for manager_roles
-- ----------------------------
DROP TABLE IF EXISTS `manager_roles`;
CREATE TABLE `manager_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `add_time` datetime NOT NULL,
  `add_user` varchar(50) NOT NULL,
  `disabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_roles
-- ----------------------------
INSERT INTO `manager_roles` VALUES ('1', '1', '2018-12-22 18:01:32', 'lh', '0');

-- ----------------------------
-- Table structure for user_car
-- ----------------------------
DROP TABLE IF EXISTS `user_car`;
CREATE TABLE `user_car` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_car_goods_id_cedc7db9_fk_goods_goodsinfo_id` (`goods_id`),
  KEY `user_car_users_id_deb1cd9d_fk_user_users_id` (`users_id`),
  CONSTRAINT `user_car_goods_id_cedc7db9_fk_goods_goodsinfo_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_goodsinfo` (`id`),
  CONSTRAINT `user_car_users_id_deb1cd9d_fk_user_users_id` FOREIGN KEY (`users_id`) REFERENCES `user_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_car
-- ----------------------------

-- ----------------------------
-- Table structure for user_comment
-- ----------------------------
DROP TABLE IF EXISTS `user_comment`;
CREATE TABLE `user_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  `content` varchar(100) NOT NULL,
  `add_time` datetime NOT NULL,
  `status` tinyint(1) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `manager_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_comment_goods_id_fde71de4_fk_goods_goodsinfo_id` (`goods_id`),
  KEY `user_comment_manager_id_a8402607_fk_manager_managermessage_id` (`manager_id`),
  KEY `user_comment_users_id_539052c5_fk_user_users_id` (`users_id`),
  CONSTRAINT `user_comment_goods_id_fde71de4_fk_goods_goodsinfo_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_goodsinfo` (`id`),
  CONSTRAINT `user_comment_manager_id_a8402607_fk_manager_managermessage_id` FOREIGN KEY (`manager_id`) REFERENCES `manager_managermessage` (`id`),
  CONSTRAINT `user_comment_users_id_539052c5_fk_user_users_id` FOREIGN KEY (`users_id`) REFERENCES `user_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_comment
-- ----------------------------

-- ----------------------------
-- Table structure for user_orders
-- ----------------------------
DROP TABLE IF EXISTS `user_orders`;
CREATE TABLE `user_orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_code` varchar(14) NOT NULL,
  `money` decimal(10,2) NOT NULL,
  `add_time` datetime NOT NULL,
  `address` varchar(150) NOT NULL,
  `contacts` varchar(30) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `pay_status` tinyint(1) NOT NULL,
  `pay_time` datetime DEFAULT NULL,
  `send_status` tinyint(1) NOT NULL,
  `send_time` datetime DEFAULT NULL,
  `receive_status` tinyint(1) NOT NULL,
  `receive_time` datetime DEFAULT NULL,
  `comment_status` tinyint(1) NOT NULL,
  `manage_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_code` (`order_code`),
  KEY `user_orders_manage_id_aaf60119_fk_manager_managermessage_id` (`manage_id`),
  KEY `user_orders_users_id_9e624e7a_fk_user_users_id` (`users_id`),
  CONSTRAINT `user_orders_manage_id_aaf60119_fk_manager_managermessage_id` FOREIGN KEY (`manage_id`) REFERENCES `manager_managermessage` (`id`),
  CONSTRAINT `user_orders_users_id_9e624e7a_fk_user_users_id` FOREIGN KEY (`users_id`) REFERENCES `user_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_orders
-- ----------------------------
INSERT INTO `user_orders` VALUES ('1', '20181010290660', '98.00', '2019-04-13 11:37:49', '河南省新乡市红旗区华兰大道东段河南科技学院', '刘欢', '18737307883', '0', null, '0', null, '0', null, '0', '5', '1');

-- ----------------------------
-- Table structure for user_order_info
-- ----------------------------
DROP TABLE IF EXISTS `user_order_info`;
CREATE TABLE `user_order_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_order_info_goods_id_e9ad180e_fk_goods_goodsinfo_id` (`goods_id`),
  KEY `user_order_info_order_id_65c5c3a2_fk_user_orders_id` (`order_id`),
  CONSTRAINT `user_order_info_goods_id_e9ad180e_fk_goods_goodsinfo_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_goodsinfo` (`id`),
  CONSTRAINT `user_order_info_order_id_65c5c3a2_fk_user_orders_id` FOREIGN KEY (`order_id`) REFERENCES `user_orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_order_info
-- ----------------------------
INSERT INTO `user_order_info` VALUES ('1', '1', '98.00', '3', '1');

-- ----------------------------
-- Table structure for user_users
-- ----------------------------
DROP TABLE IF EXISTS `user_users`;
CREATE TABLE `user_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `is_activate` tinyint(1) NOT NULL,
  `password` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_users
-- ----------------------------
INSERT INTO `user_users` VALUES ('1', 'admin', '18737307883@sina.cn', '0', '96e79218965eb72c92a549dd5a330112');

-- ----------------------------
-- Table structure for user_user_address
-- ----------------------------
DROP TABLE IF EXISTS `user_user_address`;
CREATE TABLE `user_user_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(150) NOT NULL,
  `name` varchar(30) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_user_address_users_id_1c710791_fk_user_users_id` (`users_id`),
  CONSTRAINT `user_user_address_users_id_1c710791_fk_user_users_id` FOREIGN KEY (`users_id`) REFERENCES `user_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_user_address
-- ----------------------------
INSERT INTO `user_user_address` VALUES ('1', '河南省新乡市红旗区华兰大道东段河南科技学院', '刘欢', '18737307883', '1');
