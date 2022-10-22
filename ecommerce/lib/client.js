import sanityClient from "@sanity/client";
import imageURLBuilder from "@sanity/image-url";

export const client = sanityClient({
    projectId: 'vfxfwnaw',
    dataset: 'production',
    apiVersion: '2022-03-10',
    useCdn: true,
    token: process.env.NEXT_PUBLIC_SUNITY_TOKEN
});
const builder = imageURLBuilder(client);

export const urlFor = (source) => builder.image(source);