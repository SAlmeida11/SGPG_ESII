SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`combustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`combustivel` (
  `idcombustivel` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `preco_litro` FLOAT NOT NULL,
  `categoria` VARCHAR(45) NULL,
  `quantidade_disponivel` FLOAT NULL,
  PRIMARY KEY (`idcombustivel`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Bomba`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Bomba` (
  `idBomba` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `idCombustivel` INT NOT NULL,
  PRIMARY KEY (`idBomba`),
  INDEX `fk_Bomba_combustivel_idx` (`idCombustivel` ASC) VISIBLE,
  CONSTRAINT `fk_Bomba_combustivel`
    FOREIGN KEY (`idCombustivel`)
    REFERENCES `mydb`.`combustivel` (`idcombustivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`reservatorio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`reservatorio` (
  `idReservatorio` INT NOT NULL,
  `capacidade` VARCHAR(45) NOT NULL,
  `nivel` FLOAT NOT NULL,
  `temperatura` FLOAT NOT NULL,
  `idCombustivel` INT NOT NULL,
  PRIMARY KEY (`idReservatorio`),
  INDEX `fk_reservatorio_combustivel1_idx` (`idCombustivel` ASC) VISIBLE,
  CONSTRAINT `fk_reservatorio_combustivel1`
    FOREIGN KEY (`idCombustivel`)
    REFERENCES `mydb`.`combustivel` (`idcombustivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`vendaCombustivel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`vendaCombustivel` (
  `tipo_combustivel` VARCHAR(45) NOT NULL,
  `Bomba_idBomba` INT NOT NULL,
  PRIMARY KEY (`tipo_combustivel`),
  INDEX `fk_Venda_combustivel_Bomba1_idx` (`Bomba_idBomba` ASC) VISIBLE,
  CONSTRAINT `fk_Venda_combustivel_Bomba1`
    FOREIGN KEY (`Bomba_idBomba`)
    REFERENCES `mydb`.`Bomba` (`idBomba`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`InstituiicaoCartaoCred`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`InstituiicaoCartaoCred` (
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
-- Table `mydb`.`Pagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Pagamento` (
  `id_pagamento` VARCHAR(45) NOT NULL,
  `Valor` FLOAT NOT NULL,
  `FormaPagamento` VARCHAR(45) NOT NULL,
  `Parcelado` TINYINT NOT NULL,
  `Desconto` FLOAT NULL,
  `Juros` FLOAT NULL,
  `InstituiicaoCartaoCred_cnpj` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_pagamento`),
  UNIQUE INDEX `id_oagamento_UNIQUE` (`id_pagamento` ASC) VISIBLE,
  INDEX `fk_Pagamento_InstituiicaoCartaoCred1_idx` (`InstituiicaoCartaoCred_cnpj` ASC) VISIBLE,
  CONSTRAINT `fk_Pagamento_InstituiicaoCartaoCred1`
    FOREIGN KEY (`InstituiicaoCartaoCred_cnpj`)
    REFERENCES `mydb`.`InstituiicaoCartaoCred` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`endereco`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`endereco` (
  `id_endereco` INT NOT NULL,
  `logradouro` VARCHAR(45) NOT NULL,
  `numero` INT NOT NULL,
  `bairro` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  `cep` VARCHAR(9) NOT NULL,
  PRIMARY KEY (`id_endereco`),
  UNIQUE INDEX `id_endereco_UNIQUE` (`id_endereco` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cliente` (
  `cpf` VARCHAR(45) NOT NULL,
  `nomeCliente` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `dataCadastro` DATE NOT NULL,
  `endereco_id_endereco` INT NOT NULL,
  PRIMARY KEY (`cpf`, `dataCadastro`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  INDEX `fk_cliente_endereco1_idx` (`endereco_id_endereco` ASC) VISIBLE,
  CONSTRAINT `fk_cliente_endereco1`
    FOREIGN KEY (`endereco_id_endereco`)
    REFERENCES `mydb`.`endereco` (`id_endereco`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`vinculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`vinculo` (
  `id_vinculo` VARCHAR(45) NOT NULL,
  `dtContratacao` DATE NOT NULL,
  `salario` FLOAT NOT NULL,
  `status` TINYINT NOT NULL,
  PRIMARY KEY (`id_vinculo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`funcionario` (
  `nomeFun` VARCHAR(45) NOT NULL,
  `dtNascimento` DATE NOT NULL,
  `cpf` VARCHAR(45) NOT NULL,
  `admin` TINYINT NOT NULL,
  `vinculo_id_vinculo` VARCHAR(45) NOT NULL,
  `endereco_id_endereco` INT NOT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  INDEX `fk_funcionario_vinculo1_idx` (`vinculo_id_vinculo` ASC) VISIBLE,
  INDEX `fk_funcionario_endereco1_idx` (`endereco_id_endereco` ASC) VISIBLE,
  CONSTRAINT `fk_funcionario_vinculo1`
    FOREIGN KEY (`vinculo_id_vinculo`)
    REFERENCES `mydb`.`vinculo` (`id_vinculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_funcionario_endereco1`
    FOREIGN KEY (`endereco_id_endereco`)
    REFERENCES `mydb`.`endereco` (`id_endereco`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`venda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`venda` (
  `id_venda` INT NOT NULL,
  `data_hora` DATETIME NOT NULL,
  `Venda_combustivel_tipo_combustivel` VARCHAR(45) NOT NULL,
  `Pagamento_id_pagamento` VARCHAR(45) NOT NULL,
  `cliente_cpf` VARCHAR(45) NOT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_venda`),
  INDEX `fk_venda_Venda_combustivel1_idx` (`Venda_combustivel_tipo_combustivel` ASC) VISIBLE,
  INDEX `fk_venda_Pagamento1_idx` (`Pagamento_id_pagamento` ASC) VISIBLE,
  UNIQUE INDEX `Pagamento_id_pagamento_UNIQUE` (`Pagamento_id_pagamento` ASC) VISIBLE,
  INDEX `fk_venda_cliente1_idx` (`cliente_cpf` ASC) VISIBLE,
  INDEX `fk_venda_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_venda_Venda_combustivel1`
    FOREIGN KEY (`Venda_combustivel_tipo_combustivel`)
    REFERENCES `mydb`.`vendaCombustivel` (`tipo_combustivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_Pagamento1`
    FOREIGN KEY (`Pagamento_id_pagamento`)
    REFERENCES `mydb`.`Pagamento` (`id_pagamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_cliente1`
    FOREIGN KEY (`cliente_cpf`)
    REFERENCES `mydb`.`cliente` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`fornecedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`fornecedor` (
  `cnpj` INT NOT NULL,
  `NomeFor` VARCHAR(45) NOT NULL,
  `Encarregado` VARCHAR(45) NULL,
  `Status` VARCHAR(45) NULL,
  `produtosFornecidos[]` VARCHAR(45) NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cnpj`),
  INDEX `fk_fornecedor_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_fornecedor_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`contato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`contato` (
  `id_contato` INT NOT NULL,
  `ddd` VARCHAR(3) NOT NULL,
  `telofone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `cliente_cpf` VARCHAR(45) NOT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  `fornecedor_cnpj` INT NOT NULL,
  PRIMARY KEY (`id_contato`),
  UNIQUE INDEX `id_contato_UNIQUE` (`id_contato` ASC) VISIBLE,
  INDEX `fk_contato_cliente1_idx` (`cliente_cpf` ASC) VISIBLE,
  INDEX `fk_contato_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  INDEX `fk_contato_fornecedor1_idx` (`fornecedor_cnpj` ASC) VISIBLE,
  CONSTRAINT `fk_contato_cliente1`
    FOREIGN KEY (`cliente_cpf`)
    REFERENCES `mydb`.`cliente` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contato_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contato_fornecedor1`
    FOREIGN KEY (`fornecedor_cnpj`)
    REFERENCES `mydb`.`fornecedor` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ponto_trabalho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ponto_trabalho` (
  `id_ponto` INT NOT NULL,
  `dataRegistro` DATE NOT NULL,
  `hora_chegada` TIME NOT NULL,
  `hora_saida` TIME NULL,
  `horas_trabalhadas` INT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_ponto`),
  INDEX `fk_ponto_trabalho_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_ponto_trabalho_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ordemServico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ordemServico` (
  `idordemServico` INT NOT NULL,
  `DataSolicitacao` DATE NOT NULL,
  `DataConclusao` VARCHAR(45) NOT NULL,
  `HorarioMarcado` VARCHAR(45) NOT NULL,
  `Observacoes` VARCHAR(45) NULL,
  `descricao` VARCHAR(45) NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NULL,
  `itensadicionais[]` VARCHAR(45) NULL,
  PRIMARY KEY (`idordemServico`),
  INDEX `fk_ordemServico_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  INDEX `fk_ordemServico_cliente1_idx` (`cliente_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_ordemServico_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ordemServico_cliente1`
    FOREIGN KEY (`cliente_cpf`)
    REFERENCES `mydb`.`cliente` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Servico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Servico` (
  `idServico` INT NOT NULL,
  `Descricao` VARCHAR(45) NULL,
  `Valor` FLOAT NOT NULL,
  `DuracaoEstimada` TIME NOT NULL,
  `Disponivel` TINYINT NOT NULL,
  PRIMARY KEY (`idServico`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`agendamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`agendamento` (
  `Servico_idServico` INT NOT NULL,
  `ordemServico_idordemServico` INT NOT NULL,
  `idagedamento` INT NOT NULL,
  PRIMARY KEY (`Servico_idServico`, `ordemServico_idordemServico`, `idagedamento`),
  INDEX `fk_Servico_has_ordemServico_ordemServico1_idx` (`ordemServico_idordemServico` ASC) VISIBLE,
  INDEX `fk_Servico_has_ordemServico_Servico1_idx` (`Servico_idServico` ASC) VISIBLE,
  CONSTRAINT `fk_Servico_has_ordemServico_Servico1`
    FOREIGN KEY (`Servico_idServico`)
    REFERENCES `mydb`.`Servico` (`idServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Servico_has_ordemServico_ordemServico1`
    FOREIGN KEY (`ordemServico_idordemServico`)
    REFERENCES `mydb`.`ordemServico` (`idordemServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`item` (
  `iditem` INT NOT NULL,
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
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`solicitacaoRemessa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`solicitacaoRemessa` (
  `idsolicitacaoRemessa` INT NOT NULL,
  `DataSolicitacao` DATE NOT NULL,
  `DataEntrega` DATE NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `fornecedor_cnpj` INT NOT NULL,
  `funcionario_cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsolicitacaoRemessa`),
  INDEX `fk_solicitacaoRemessa_fornecedor1_idx` (`fornecedor_cnpj` ASC) VISIBLE,
  INDEX `fk_solicitacaoRemessa_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_solicitacaoRemessa_fornecedor1`
    FOREIGN KEY (`fornecedor_cnpj`)
    REFERENCES `mydb`.`fornecedor` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solicitacaoRemessa_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `mydb`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`entrega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`entrega` (
  `fornecedor_cnpj` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `identrega` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`fornecedor_cnpj`, `item_iditem`, `identrega`),
  INDEX `fk_fornecedor_has_item_item1_idx` (`item_iditem` ASC) VISIBLE,
  INDEX `fk_fornecedor_has_item_fornecedor1_idx` (`fornecedor_cnpj` ASC) VISIBLE,
  CONSTRAINT `fk_fornecedor_has_item_fornecedor1`
    FOREIGN KEY (`fornecedor_cnpj`)
    REFERENCES `mydb`.`fornecedor` (`cnpj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fornecedor_has_item_item1`
    FOREIGN KEY (`item_iditem`)
    REFERENCES `mydb`.`item` (`iditem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`itemvenda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`itemvenda` (
  `Quantidade` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `venda_id_venda` INT NOT NULL,
  `iditemVenda` VARCHAR(45) NOT NULL,
  INDEX `fk_itemvenda_item1_idx` (`item_iditem` ASC) VISIBLE,
  INDEX `fk_itemvenda_venda1_idx` (`venda_id_venda` ASC) VISIBLE,
  PRIMARY KEY (`iditemVenda`),
  CONSTRAINT `fk_itemvenda_item1`
    FOREIGN KEY (`item_iditem`)
    REFERENCES `mydb`.`item` (`iditem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_itemvenda_venda1`
    FOREIGN KEY (`venda_id_venda`)
    REFERENCES `mydb`.`venda` (`id_venda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
