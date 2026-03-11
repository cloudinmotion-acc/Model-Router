output "model_router_output" {
  description = "LLM ComponentAsset outputs."
  value = {
    namespace           = kubernetes_namespace_v1.namespace.metadata[0].name
    server_service_name  = kubernetes_service_v1.server_service.metadata[0].name
    server_service_port = kubernetes_service_v1.server_service.spec[0].port[0].port
    deployment_name     = kubernetes_deployment_v1.server_app.metadata[0].name
    replica_count       = kubernetes_deployment_v1.server_app.spec[0].replicas
    image_used          = var.image
    llm_provider        = var.llm_provider
  }
}
output "mpp_report" {
  description = "LLM ComponentAsset outputs."
  value = {
    namespace           = kubernetes_namespace_v1.namespace.metadata[0].name
    server_service_name   = kubernetes_service_v1.server_service.metadata[0].name
    server_service_port = kubernetes_service_v1.server_service.spec[0].port[0].port
    deployment_name     = kubernetes_deployment_v1.server_app.metadata[0].name
    replica_count       = kubernetes_deployment_v1.server_app.spec[0].replicas
    image_used          = var.image
    llm_provider        = var.llm_provider
  }
}  