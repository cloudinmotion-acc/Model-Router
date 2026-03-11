variable "platform_output" {
  description = "User provided inputs for myPlatform deployment"
  type = object({
    name             = string
    system_name      = string
    environment_type = string
    owner            = string
    tags             = map(string)
  })
  default     = null
}

variable "bastion_host_output" {
  description = "Not used, placeholder to satisfy auto-generated main.tf.json"
  type        = any
  default     = null
}

variable "initialization_output" {
  description = "Not used, placeholder to satisfy auto-generated main.tf.json"
  type        = any
  default     = null
}

variable "kubernetes_cluster_output" {
  description = "Not used, placeholder to satisfy auto-generated main.tf.json"
  type        = any
  default     = null
}

variable "image" {
  description = "Docker image to use for the application"
  type        = string
  default     = "310378384655.dkr.ecr.us-east-1.amazonaws.com/llm-module:v1.3"
}

variable "api_key" {
  type      = string
  sensitive = true
}

variable "llm_provider" {
  description = "LLM provider (openai, gemini, claude, etc.)"
  type        = string
}

variable "replicas" {
  description = "Number of replicas"
  type        = number
  default     = 3
}


variable "pod_port" {
  description = "server port inside the pod"
  type        = number
  default     = 8000
}

variable "server_port" {
  description = "kubernetes service port "
  type        = number
  default     = 8000
}