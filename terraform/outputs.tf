output "namespace" {
  value = kubernetes_namespace_v1.namespace.metadata[0].name
}
output "server_service_ip" {
  value = kubernetes_service_v1.server_service.spec[0].cluster_ip
}
output "server_service_port" {
  value = kubernetes_service_v1.server_service.spec[0].port[0].port
}
output "deployment_name" {
  value = kubernetes_deployment_v1.server_app.metadata[0].name
}
output "replica_count" {
  value = kubernetes_deployment_v1.server_app.spec[0].replicas
}
output "image_used" {
  value = var.image
}
