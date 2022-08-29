from calculator_pb2_grpc import CalculatorServicer

from calculator_pb2 import SumRequest
from calculator_pb2 import SumReply
from calculator_pb2 import MultiplyRequest
from calculator_pb2 import MultiplyReply
from calculator_pb2 import Max3Request
from calculator_pb2 import Max3Reply
from calculator_pb2 import DivModRequest
from calculator_pb2 import DivModReply
from grpc import ServicerContext


class Calculator(CalculatorServicer):

    def Sum(self, request: SumRequest, context: ServicerContext) -> SumReply:
        return SumReply(s=request.a + request.b)
    def Multiply(self, request: MultiplyRequest, context: ServicerContext) -> MultiplyReply:
        return MultiplyReply(s=request.a * request.b)
    def Max3(self, request: Max3Request, context: ServicerContext) -> Max3Reply:
        return Max3Reply(s=max(request.a, request.b, request.c))

    def DivMod(self, request: DivModRequest, context: ServicerContext) -> DivModReply:
        return DivModReply(div=request.a//request.b, mod=request.a%request.b)
