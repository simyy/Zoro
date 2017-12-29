# 创建数据库
create database `zoro`;

# 用户 
create table `user` (
    `id` bigint(64) not null auto_increment primary key, 
    `appId` int(1) not null comment '应用ID',
    `mobile` varchar(64) default null comment '手机号',
    `unionId` varchar(64) not null comment '微信唯一ID',
    `nickName` varchar(256) not null comment '用户昵称',
    `avatarUrl` varchar(1024) not null comment '用户头像',
    `gender` int(1) not null comment '性别： 0未知、1男、2女',
    `province` varchar(128) default null comment '省份',
    `city` varchar(128) default null comment '城市',
    `country` varchar(128) default null comment '国家',
    `isDeleted` int(1) default 0 comment '1已删除 0未删除',
    `gmtModify` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NULL COMMENT '更新时间', 
    `gmtCreate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
    KEY `idx_unionId` (`unionId`),
    KEY `idx_mobile` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 comment '用户';
