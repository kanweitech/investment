Issues that needs to be resolved before migrating:

#### SQL COMMANDS

- Updates Extra ridiculous high pending figures e.g 800,000,000,000,000,000
  `` UPDATE `investments` SET `investments`.`amount`='1000000000' WHERE CAST(amount AS DECIMAL(50)) > 1000000000; ``
