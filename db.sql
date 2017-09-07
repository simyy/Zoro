# 创建数据库
create database `Zoro`;

# 用户 
create table `user` (
    `id` bigint(64) not null auto_increment primary key, 
    `unionId` varchar(256) not null comment '微信唯一ID',
    `nickName` varchar(256) not null comment '用户昵称',
    `avatarUrl` varchar(1024) not null comment '用户头像',
    `gender` int(1) not null comment '性别： 0未知、1男、2女',
    `province` varchar(128) default null comment '省份',
    `city` varchar(128) default null comment '城市',
    `country` varchar(128) default null comment '国家',
    `gmtModify` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NULL COMMENT '更新时间', 
    `gmtCreate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
    KEY `idx_unionId` (`unionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 comment '用户';

# 喝水记录
create table `drink_record` (
    `id` bigint(64) not null auto_increment primary key,
    `userId` bigint(64) not null comment '用户ID',
    `status` int(1) not null comment '状态: -1已删除、0初始、1已完成、2已过期',
    `expireTime` datetime not null comment '过期时间',
    `gmtModify` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NULL COMMENT '更新时间', 
    `gmtCreate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
    KEY `idx_userId_status` (`userId`, `status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 comment '喝水记录';
