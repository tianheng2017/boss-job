/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80016
Source Host           : localhost:3306
Source Database       : boss

Target Server Type    : MYSQL
Target Server Version : 80016
File Encoding         : 65001

Date: 2020-03-30 23:39:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for zp_position
-- ----------------------------
DROP TABLE IF EXISTS `zp_position`;
CREATE TABLE `zp_position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT '0' COMMENT '上级ID',
  `level` tinyint(1) DEFAULT '1' COMMENT '职位级别 1第一层职位 2第二层职位 3第三层职位',
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '职位名称',
  `hide` tinyint(1) DEFAULT '0' COMMENT '0显示1隐藏',
  `state` tinyint(1) DEFAULT '1' COMMENT '状态0禁用1启用',
  `update_time` int(11) DEFAULT '0' COMMENT '更新时间',
  `create_time` int(11) DEFAULT '0' COMMENT '创建时间',
  `delete_time` int(11) DEFAULT '0' COMMENT '删除时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1032 DEFAULT CHARSET=utf8;
