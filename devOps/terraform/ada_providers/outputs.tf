#  -------------------- Retornos do Provedor  -------------------- 
output "ip_privado" {
  value       = aws_instance.web.private_ip
  sensitive   = true
  description = "Recuperar o IPV4 privado da instância"
  depends_on  = []
}