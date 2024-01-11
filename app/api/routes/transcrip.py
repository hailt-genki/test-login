from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies.transcrip import init_detector
from app.models.schemas.detect_response import ProfileInResponse
from app.models.domain.profiles import Profile, Item
from starlette import status

router = APIRouter()
detector = init_detector()


@router.post(
    "/detect",
    response_model=ProfileInResponse,
    name="detect:profile",
    status_code=status.HTTP_201_CREATED,
)
async def detecting(
    req: Item,
) -> ProfileInResponse:
    detection_result = detector.detect(req.input_text)
    
    probability = 0
    language_code = ""
    for detection in detection_result.detections:
        # print(f'{detection.language_code}: ({detection.probability:.2f})')
        if detection.probability > probability:
            language_code = detection.language_code
            probability = detection.probability
    fil = Profile(language_code = language_code,probability=round(probability,2))
    return ProfileInResponse(profile=fil)
