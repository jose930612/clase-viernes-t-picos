DROP TABLE IF EXISTS `estados_civiles`;
CREATE TABLE IF NOT EXISTS `estados_civiles` (
	`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	`descripcion` varchar(220) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;

INSERT INTO `estados_civiles` (`descripcion`) VALUES ('Soltero');
INSERT INTO `estados_civiles` (`descripcion`) VALUES ('Casado');
INSERT INTO `estados_civiles` (`descripcion`) VALUES ('Union libre');
INSERT INTO `estados_civiles` (`descripcion`) VALUES ('Divorciado');

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) unsigned NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `genero` varchar(2) NOT NULL,
  `fecha_nacimiento` datetime DEFAULT NULL,
  `estado_civil` int(11) unsigned,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`estado_civil`) REFERENCES estados_civiles(`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;

DROP TABLE IF EXISTS `estados_facturas`;
CREATE TABLE IF NOT EXISTS `estados_facturas` (
	`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	`descripcion` varchar(220) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;

INSERT INTO `estados_facturas` (`descripcion`) VALUES ('Pagada');
INSERT INTO `estados_facturas` (`descripcion`) VALUES ('Cancelada');
INSERT INTO `estados_facturas` (`descripcion`) VALUES ('Pendiente');

DROP TABLE IF EXISTS `tipos_item`;
CREATE TABLE IF NOT EXISTS `tipos_item` (
	`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	`descripcion` varchar(220) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;

INSERT INTO `tipos_item` (`descripcion`) VALUES ('Ropa');
INSERT INTO `tipos_item` (`descripcion`) VALUES ('Enlatado');
INSERT INTO `tipos_item` (`descripcion`) VALUES ('Bebida');
INSERT INTO `tipos_item` (`descripcion`) VALUES ('Mecato');
INSERT INTO `tipos_item` (`descripcion`) VALUES ('Carne');

DROP TABLE IF EXISTS `items`;
CREATE TABLE IF NOT EXISTS `items` (
	`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	`tipo_item` int(11) unsigned,
	`descripcion` varchar(220) NOT NULL,
	`valor_unidad` float(11) unsigned NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`tipo_item`) REFERENCES tipos_item(`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;

INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (1,'Hoodie', 90.000);
INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (1,'jean', 50.000);
INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (5,'carne hamburguesa', 78.00);
INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (4,'papas BBQ', 2.300);
INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (4,'papas Pollo', 2.300);
INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (3,'Coca-cola', 2.500);
INSERT INTO `items` (`tipo_item`, `descripcion`, `valor_unidad`) VALUES (3,'Pepsi', 2.500);

DROP TABLE IF EXISTS `facturas`;
CREATE TABLE IF NOT EXISTS `facturas` (
  `no_factura` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Fecha_factura` datetime DEFAULT NULL,
  `cliente` int(11) unsigned,
  `total_factura` int(11) unsigned NOT NULL,
  `estado` int(11) unsigned,
  PRIMARY KEY (`no_factura`),
  FOREIGN KEY (`cliente`) REFERENCES clientes(`id`),
  FOREIGN KEY (`estado`) REFERENCES estados_facturas(`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;



DROP TABLE IF EXISTS `items_factura`;
CREATE TABLE IF NOT EXISTS `items_factura` (
	`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	`id_factura` int(11) unsigned,
	`id_item` int(11) unsigned,
	`cantidad` int(11) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`id_factura`) REFERENCES facturas(`no_factura`),
	FOREIGN KEY (`id_item`) REFERENCES items(`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0;