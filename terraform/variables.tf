variable "image" {
  description = "Docker image to use for the application"
  type        = string
}

variable "openai_api_key" {
  type      = string
  sensitive = true
}

variable "replicas" {
  description = "Number of replicas"
  type        = number
  default     = 2
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