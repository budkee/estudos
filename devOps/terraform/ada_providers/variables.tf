variable "aws_region" {
  type        = string
  default     = "eu-west-1"
  description = "Instância Padrão da AWS"
}

variable "instance_name" {
  type        = string
  default     = "ada_treinamento_terraform"
  description = "Nome da Instância"
}

variable "vpc_name" {
  type        = string
  default     = "vpc_treinamento_ada"
  description = "VPC criada por módulos"
}