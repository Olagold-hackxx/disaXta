
target "dapp" {
}

variable "TAG" {
  default = "devel"
}

variable "DOCKER_ORGANIZATION" {
  default = "cartesi"
}

target "server" {
  tags = ["${DOCKER_ORGANIZATION}/dapp:donation-${TAG}-server"]
}

target "console" {
  tags = ["${DOCKER_ORGANIZATION}/dapp:donation-${TAG}-console"]
}

target "machine" {
  tags = ["${DOCKER_ORGANIZATION}/dapp:donation-${TAG}-machine"]
}
