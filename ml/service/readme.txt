# bsgo 서비스를 통해 번역된 데이터를 저장하는 테이블
# 향후 적정량이 모이면 학습용으로 사용된다.

CREATE TABLE `tbl_trans_lang_log` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`oCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '언어감지코드',
	`tCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '번역결과언어코드',
	`oStr` TEXT NULL DEFAULT NULL COMMENT '원문',
	`tStr` TEXT NULL DEFAULT NULL COMMENT '번역문',
	`regDate` TIMESTAMP NULL DEFAULT NULL ON UPDATE current_timestamp(),
	PRIMARY KEY (`id`)
)
COMMENT='bsgo 사이트를 사용한 번역 로그 테이블\r\n해당 데이터는 어느정도 쌓이면 학습용 데이터로 사용된다'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=2
;

# 데이터 추가
INSERT INTO `py_db`.`tbl_trans_lang_log`
 (`oCode`, `tCode`, `oStr`, `tStr`)
 VALUES 
 ('en', 'ko', 'hello', '안녕');
