SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb2` DEFAULT CHARACTER SET utf8;
USE `mydb2` ;

-- -----------------------------------------------------
-- Table `mydb2`.`combustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`combustivel` (
  `idcombustivel` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `preco_litro` DECIMAL(10,2) NOT NULL,
  `categoria` VARCHAR(45) NULL,
  `quantidade_disponivel` DECIMAL(10,2) NULL,
  PRIMARY KEY (`idcombustivel`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`Bomba`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`Bomba` (
  `idBomba` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `idCombustivel` INT NOT NULL,
  PRIMARY KEY (`idBomba`),
  INDEX `fk_Bomba_combustivel_idx` (`idCombustivel` ASC) VISIBLE,
  CONSTRAINT `fk_Bomba_combustivel`
    FOREIGN KEY (`idCombustivel`)
    REFERENCES `mydb2`.`combustivel` (`idcombustivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`reservatorio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`reservatorio` (
  `idReservatorio` INT NOT NULL AUTO_INCREMENT,
  `capacidade` DECIMAL(10,2) NOT NULL,
  `nivel` DECIMAL(10,2) NOT NULL,
  `temperatura` DECIMAL(5,2) NOT NULL,
  `idCombustivel` INT NOT NULL,
  PRIMARY KEY (`idReservatorio`),
  INDEX `fk_reservatorio_combustivel1_idx` (`idCombustivel` ASC) VISIBLE,
  CONSTRAINT `fk_reservatorio_combustivel1`
    FOREIGN KEY (`idCombustivel`)
    REFERENCES `mydb2`.`combustivel` (`idcombustivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`vendaCombustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`vendaCombustivel` (
  `idvendaCombustivel` INT NOT NULL AUTO_INCREMENT,
  `tipo_combustivel` VARCHAR(45) NOT NULL,
  `Bomba_idBomba` INT NOT NULL,
  PRIMARY KEY (`idvendaCombustivel`),
  INDEX `fk_Venda_combustivel_Bomba1_idx` (`Bomba_idBomba` ASC) VISIBLE,
  CONSTRAINT `fk_Venda_combustivel_Bomba1`
    FOREIGN KEY (`Bomba_idBomba`)
    REFERENCES `mydb2`.`Bomba` (`idBomba`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`InstituiicaoCartaoCred`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`InstituiicaoCartaoCred` (
  `cnpj` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `bandeira` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `status` TINYINT NOT NULL,
  PRIMARY KEY (`cnpj`),
  UNIQUE INDEX `idInstituicaoCartaoCred_UNIQUE` (`cnpj` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`Pagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`Pagamento` (
  `id_pagamento` INT NOT NULL AUTO_INCREMENT,
  `Valor` FLOAT NOT NULL,
  `FormaPagamento` VARCHAR(45) NOT NULL,
  `Parcelado` TINYINT NOT NULL,
  `Desconto` FLOAT NULL,
  `Juros` FLOAT NULL,
  `InstituiicaoCartaoCred_cnpj` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_pagamento`),
  INDEX `fk_Pagamento_InstituiicaoCartaoCred1_idx` (`InstituiicaoCartaoCred_cnpj` ASC) VISIBLE,
  CONSTRAINT `fk_Pagamento_InstituiicaoCartaoCred1`
    FOREIGN KEY (`InstituiicaoCartaoCred_cnpj`)
    REFERENCES `mydb2`.`InstituiicaoCartaoCred` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`endereco`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`endereco` (
  `id_endereco` INT NOT NULL AUTO_INCREMENT,
  `logradouro` VARCHAR(45) NOT NULL,
  `numero` INT NOT NULL,
  `bairro` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  `cep` VARCHAR(9) NOT NULL,
  PRIMARY KEY (`id_endereco`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`vinculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`vinculo` (
  `id_vinculo` INT NOT NULL AUTO_INCREMENT,
  `dtContratacao` DATE NOT NULL,
  `salario` FLOAT NOT NULL,
  `status` TINYINT NOT NULL,
  PRIMARY KEY (`id_vinculo`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`cliente` (
  `cpf` VARCHAR(45) NOT NULL,
  `nomeCliente` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `dataCadastro` DATE NOT NULL,
  `endereco_id_endereco` INT NOT NULL,
  PRIMARY KEY (`cpf`),
  INDEX `fk_cliente_endereco1_idx` (`endereco_id_endereco` ASC) VISIBLE,
  CONSTRAINT `fk_cliente_endereco1`
    FOREIGN KEY (`endereco_id_endereco`)
    REFERENCES `mydb2`.`endereco` (`id_endereco`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`funcionario` (
  `cpf` VARCHAR(45) NOT NULL,
  `nomeFun` VARCHAR(45) NOT NULL,
  `dtNascimento` DATE NOT NULL,
  `admin` TINYINT NOT NULL,
  `vinculo_id_vinculo` INT NOT NULL,
  `endereco_id_endereco` INT NOT NULL,
  PRIMARY KEY (`cpf`),
  INDEX `fk_funcionario_vinculo1_idx` (`vinculo_id_vinculo` ASC) VISIBLE,
  INDEX `fk_funcionario_endereco1_idx` (`endereco_id_endereco` ASC) VISIBLE,
  CONSTRAINT `fk_funcionario_vinculo1`
    FOREIGN KEY (`vinculo_id_vinculo`)
    REFERENCES `mydb2`.`vinculo` (`id_vinculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_funcionario_endereco1`
    FOREIGN KEY (`endereco_id_endereco`)
    REFERENCES `mydb2`.`endereco` (`id_endereco`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`venda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`venda` (
  `id_venda` INT NOT NULL AUTO_INCREMENT,
  `data_hora` DATETIME NOT NULL,
  `Venda_combustivel_idvendaCombustivel` INT NOT NULL,
  `Pagamento_id_pagamento` INT NOT NULL,
  `cliente_cpf` VARCHAR(45) NOT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_venda`),
  INDEX `fk_venda_Venda_combustivel1_idx` (`Venda_combustivel_idvendaCombustivel` ASC) VISIBLE,
  INDEX `fk_venda_Pagamento1_idx` (`Pagamento_id_pagamento` ASC) VISIBLE,
  INDEX `fk_venda_cliente1_idx` (`cliente_cpf` ASC) VISIBLE,
  INDEX `fk_venda_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_venda_Venda_combustivel1`
    FOREIGN KEY (`Venda_combustivel_idvendaCombustivel`)
    REFERENCES `mydb2`.`vendaCombustivel` (`idvendaCombustivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_Pagamento1`
    FOREIGN KEY (`Pagamento_id_pagamento`)
    REFERENCES `mydb2`.`Pagamento` (`id_pagamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_cliente1`
    FOREIGN KEY (`cliente_cpf`)
    REFERENCES `mydb2`.`cliente` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`fornecedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`fornecedor` (
  `cnpj` VARCHAR(45) NOT NULL,
  `NomeFor` VARCHAR(45) NOT NULL,
  `Encarregado` VARCHAR(45) NULL,
  `Status` VARCHAR(45) NULL,
  `produtosFornecidos` VARCHAR(45) NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cnpj`),
  INDEX `fk_fornecedor_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_fornecedor_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`contato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`contato` (
  `id_contato` INT NOT NULL AUTO_INCREMENT,
  `ddd` VARCHAR(3) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `cliente_cpf` VARCHAR(45) NULL,
  `funcionario_cpf` VARCHAR(45) NULL,
  `fornecedor_cnpj` VARCHAR(45) NULL,
  PRIMARY KEY (`id_contato`),
  INDEX `fk_contato_cliente1_idx` (`cliente_cpf` ASC) VISIBLE,
  INDEX `fk_contato_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  INDEX `fk_contato_fornecedor1_idx` (`fornecedor_cnpj` ASC) VISIBLE,
  CONSTRAINT `fk_contato_cliente1`
    FOREIGN KEY (`cliente_cpf`)
    REFERENCES `mydb2`.`cliente` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contato_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contato_fornecedor1`
    FOREIGN KEY (`fornecedor_cnpj`)
    REFERENCES `mydb2`.`fornecedor` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`ponto_trabalho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`ponto_trabalho` (
  `id_ponto` INT NOT NULL AUTO_INCREMENT,
  `dataRegistro` DATE NOT NULL,
  `hora_chegada` TIME NOT NULL,
  `hora_saida` TIME NULL,
  `horas_trabalhadas` INT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_ponto`),
  INDEX `fk_ponto_trabalho_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_ponto_trabalho_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`Servico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`Servico` (
  `idServico` INT NOT NULL AUTO_INCREMENT,
  `Descricao` VARCHAR(45) NULL,
  `Valor` FLOAT NOT NULL,
  `DuracaoEstimada` TIME NOT NULL,
  `Disponivel` TINYINT NOT NULL,
  PRIMARY KEY (`idServico`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`ordemServico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`ordemServico` (
  `idordemServico` INT NOT NULL AUTO_INCREMENT,
  `DataSolicitacao` DATE NOT NULL,
  `DataConclusao` VARCHAR(45) NOT NULL,
  `HorarioMarcado` VARCHAR(45) NOT NULL,
  `Observacoes` VARCHAR(45) NULL,
  `descricao` VARCHAR(45) NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NULL,
  `itensadicionais` VARCHAR(45) NULL,
  `cliente_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idordemServico`),
  INDEX `fk_ordemServico_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  INDEX `fk_ordemServico_cliente1_idx` (`cliente_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_ordemServico_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ordemServico_cliente1`
    FOREIGN KEY (`cliente_cpf`)
    REFERENCES `mydb2`.`cliente` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`agendamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`agendamento` (
  `idagendamento` INT NOT NULL AUTO_INCREMENT,
  `Servico_idServico` INT NOT NULL,
  `ordemServico_idordemServico` INT NOT NULL,
  PRIMARY KEY (`idagendamento`),
  INDEX `fk_Servico_has_ordemServico_ordemServico1_idx` (`ordemServico_idordemServico` ASC) VISIBLE,
  INDEX `fk_Servico_has_ordemServico_Servico1_idx` (`Servico_idServico` ASC) VISIBLE,
  CONSTRAINT `fk_Servico_has_ordemServico_Servico1`
    FOREIGN KEY (`Servico_idServico`)
    REFERENCES `mydb2`.`Servico` (`idServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Servico_has_ordemServico_ordemServico1`
    FOREIGN KEY (`ordemServico_idordemServico`)
    REFERENCES `mydb2`.`ordemServico` (`idordemServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`item` (
  `iditem` INT NOT NULL AUTO_INCREMENT,
  `NomeItem` VARCHAR(45) NOT NULL,
  `Categoria` VARCHAR(45) NOT NULL,
  `QtdeEstoque` INT NOT NULL,
  `PrecUnitario` FLOAT NOT NULL,
  `CodigoBarras` VARCHAR(45) NOT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iditem`),
  INDEX `fk_item_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_item_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`solicitacaoRemessa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`solicitacaoRemessa` (
  `idsolicitacaoRemessa` INT NOT NULL AUTO_INCREMENT,
  `DataSolicitacao` DATE NOT NULL,
  `DataEntrega` DATE NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `fornecedor_cnpj` VARCHAR(45) NOT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsolicitacaoRemessa`),
  INDEX `fk_solicitacaoRemessa_fornecedor1_idx` (`fornecedor_cnpj` ASC) VISIBLE,
  INDEX `fk_solicitacaoRemessa_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_solicitacaoRemessa_fornecedor1`
    FOREIGN KEY (`fornecedor_cnpj`)
    REFERENCES `mydb2`.`fornecedor` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solicitacaoRemessa_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb2`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`entrega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`entrega` (
  `identrega` INT NOT NULL AUTO_INCREMENT,
  `fornecedor_cnpj` VARCHAR(45) NOT NULL,
  `item_iditem` INT NOT NULL,
  PRIMARY KEY (`identrega`),
  INDEX `fk_fornecedor_has_item_item1_idx` (`item_iditem` ASC) VISIBLE,
  INDEX `fk_fornecedor_has_item_fornecedor1_idx` (`fornecedor_cnpj` ASC) VISIBLE,
  CONSTRAINT `fk_fornecedor_has_item_fornecedor1`
    FOREIGN KEY (`fornecedor_cnpj`)
    REFERENCES `mydb2`.`fornecedor` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fornecedor_has_item_item1`
    FOREIGN KEY (`item_iditem`)
    REFERENCES `mydb2`.`item` (`iditem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb2`.`itemvenda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`itemvenda` (
  `iditemVenda` INT NOT NULL AUTO_INCREMENT,
  `Quantidade` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `venda_id_venda` INT NOT NULL,
  PRIMARY KEY (`iditemVenda`),
  INDEX `fk_itemvenda_item1_idx` (`item_iditem` ASC) VISIBLE,
  INDEX `fk_itemvenda_venda1_idx` (`venda_id_venda` ASC) VISIBLE,
  CONSTRAINT `fk_itemvenda_item1`
    FOREIGN KEY (`item_iditem`)
    REFERENCES `mydb2`.`item` (`iditem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_itemvenda_venda1`
    FOREIGN KEY (`venda_id_venda`)
    REFERENCES `mydb2`.`venda` (`id_venda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;